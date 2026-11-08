"""Run the whole pipeline end to end.

This is the entry point for ``uv run gogdb-pipeline``. Right now it has one
stage; later stages get added below it:

    extract (GOG DB -> RustFS)
"""

from __future__ import annotations

from gogdb_pipeline import extract


def main() -> None:
    """Run the full pipeline end to end."""
    extract.extract()


if __name__ == "__main__":
    main()
