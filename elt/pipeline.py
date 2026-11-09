"""Run the whole pipeline end to end.

This is the entry point for ``uv run gogdb-pipeline``:

    extract (GOG DB -> RustFS) -> load (RustFS -> DuckDB)
"""

from __future__ import annotations

from elt import extract, load


def main() -> None:
    """Run the full pipeline end to end."""
    key = extract.extract()
    con = load.connect()
    try:
        print("Loaded:", load.load_all(con, key))
    finally:
        con.close()


if __name__ == "__main__":
    main()
