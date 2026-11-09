"""Extract: land the newest GOG DB backup in RustFS, unchanged.

GOG DB publishes a full backup every day. ``filelist.txt`` lists them oldest
first, e.g. ``2026-11/gogdb_2026-11-08.tar.xz``. We land the newest one raw,
keeping its ``.tar.xz`` name, at ``products/dt=<day>/<filename>``.

Docs:
  - GOG DB backups:   https://www.gogdb.org/backups_v3/products/
  - httpx client:     https://www.python-httpx.org/api/#client
  - boto3 put_object: https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/put_object.html
"""

from __future__ import annotations

import httpx
from botocore.client import BaseClient
from botocore.exceptions import ClientError

from elt.config import S3_BUCKET, get_http_client, get_s3_client

BACKUPS = "/backups_v3/products"


def ensure_bucket(s3: BaseClient) -> None:
    """Create the bucket on the first run, so a fresh RustFS works."""
    try:
        s3.head_bucket(Bucket=S3_BUCKET)
    except ClientError:
        s3.create_bucket(Bucket=S3_BUCKET)


def latest_backup(http: httpx.Client) -> str:
    """Return the newest backup's path, e.g. ``2026-11/gogdb_2026-11-08.tar.xz``."""
    return http.get(f"{BACKUPS}/filelist.txt").raise_for_status().text.split()[-1]


def s3_key(backup: str) -> str:
    """Turn ``2026-11/gogdb_2026-11-08.tar.xz`` into ``products/dt=2026-11-08/gogdb_2026-11-08.tar.xz``."""
    filename = backup.split("/")[-1]
    day = filename.removeprefix("gogdb_").removesuffix(".tar.xz")
    return f"products/dt={day}/{filename}"


def already_landed(s3: BaseClient, key: str) -> bool:
    """True if this backup is already in the bucket, so re-runs are safe."""
    return s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=key)["KeyCount"] > 0


def land(s3: BaseClient, key: str, data: bytes) -> None:
    """Save the backup to RustFS exactly as downloaded, labeled as xz."""
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=data, ContentType="application/x-xz")


def extract() -> str:
    """Land the newest backup in RustFS and return its S3 key."""
    s3 = get_s3_client()
    ensure_bucket(s3)
    with get_http_client() as http:
        backup = latest_backup(http)
        key = s3_key(backup)
        if already_landed(s3, key):
            print(f"Already landed: {key}")
            return key
        data = http.get(f"{BACKUPS}/{backup}").raise_for_status().content
        land(s3, key, data)
        print(f"Landed {key} ({len(data) / 1e6:.0f} MB)")
        return key


if __name__ == "__main__":
    # uv run python -m elt.extract
    extract()
