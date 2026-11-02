"""Extract: land the newest GOG DB backup in RustFS, unchanged."""

from gogdb_pipeline.config import S3_BUCKET, get_http_client, get_s3_client

BACKUPS: str = "/backups_v3/products"


def extract() -> None:
    s3 = get_s3_client()
    with get_http_client() as http:
        # filelist.txt is sorted, so the last line is the newest backup,
        # e.g. "2026-11/gogdb_2026-11-02.tar.xz"
        latest: str = (
            http.get(f"{BACKUPS}/filelist.txt").raise_for_status().text.split()[-1]
        )
        filename: str = latest.split("/")[-1]
        day: str = filename.removeprefix("gogdb_").removesuffix(".tar.xz")
        key: str = f"products/dt={day}/{filename}"

        # Skip if this backup is already in the bucket, so re-runs are safe.
        if s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=key)["KeyCount"]:
            print(f"Already landed: {key}")
            return

        data: bytes = http.get(f"{BACKUPS}/{latest}").raise_for_status().content
        s3.put_object(Bucket=S3_BUCKET, Key=key, Body=data)
        print(f"Landed {key} ({len(data) / 1e6:.0f} MB)")
