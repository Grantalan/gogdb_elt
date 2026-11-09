"""Load: read the landed backup from RustFS into DuckDB, AS-IS.

DuckDB can't read inside a ``.tar.xz``, so we unpack it into a temporary
folder that is deleted as soon as the load finishes. Each JSON file type lands
in its own ``raw_`` table; nested fields land as structs and lists.

Docs:
  - DuckDB JSON: https://duckdb.org/docs/data/json/overview
"""

from __future__ import annotations

import tarfile
import tempfile
from pathlib import Path

import duckdb

from elt.config import S3_BUCKET, get_s3_client

# The DuckDB database file the whole pipeline shares. (data/ is git-ignored.)
DB_PATH = Path("data/gogdb.duckdb")

# The product id is the folder name, e.g. products/1207658924/prices.json
PRODUCT_ID = r"regexp_extract(filename, 'products/(\d+)/', 1)::BIGINT AS product_id"


def connect(db_path: Path = DB_PATH) -> duckdb.DuckDBPyConnection:
    """Open (creating it if needed) the DuckDB database and return the connection."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the file in DuckDB 1.3 format so DataGrip's driver (1.3.1) can open it.
    return duckdb.connect(
        str(db_path), config={"storage_compatibility_version": "v1.3.0"}
    )


def load_all(con: duckdb.DuckDBPyConnection, key: str) -> dict[str, int]:
    """Load the backup at ``key`` into one raw table per file type; return the row counts."""
    with tempfile.TemporaryDirectory() as raw:
        body = get_s3_client().get_object(Bucket=S3_BUCKET, Key=key)["Body"]
        with tarfile.open(fileobj=body, mode="r|xz") as tar:
            tar.extractall(raw, filter="data")

        tables = {
            "raw_ids": f"SELECT json AS product_id FROM read_json_auto('{raw}/ids.json')",
            "raw_products": f"SELECT * FROM read_json_auto('{raw}/products/*/product.json')",
            "raw_prices": f"SELECT {PRODUCT_ID}, US FROM read_json_auto('{raw}/products/*/prices.json', filename = true)",
            "raw_prices_pre2019": f"SELECT {PRODUCT_ID}, US FROM read_json_auto('{raw}/products/*/prices_pre2019.json', filename = true)",
            "raw_changes": f"SELECT * FROM read_json_auto('{raw}/products/*/changes.json')",
            "raw_builds": f"SELECT {PRODUCT_ID}, json FROM read_json_objects('{raw}/products/*/builds/*.json', filename = true)",
        }
        for table, select in tables.items():
            con.execute(f"CREATE OR REPLACE TABLE {table} AS {select}")

    return {
        table: con.sql(f"SELECT count(*) FROM {table}").fetchall()[0][0]
        for table in tables
    }


if __name__ == "__main__":
    # uv run python -m elt.load
    from elt.extract import extract

    con = connect()
    print("loaded:", load_all(con, extract()))
    con.close()
