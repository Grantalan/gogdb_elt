## GOG ETL Pipeline

>Source: https://www.gogdb.org/

### GOGDB - Database Bulk Download (~1.1 GB)
```bash
rm -rf data/sample/products # Delete existing data - directory
mkdir -p data/sample # Make sure data/sample exists
LATEST=$(curl -s https://www.gogdb.org/backups_v3/products/filelist.txt | tail -1) # Create variable for most recent data dump
curl -s "https://www.gogdb.org/backups_v3/products/$LATEST" | tar -xJ -C data/sample # Save most up to data tar.xz sample on disk
```

* Fetch data from source
* Set up docker image YAML
* Configure httpx and botoS3 client
* Land data in RustFS

>**Must have [`uv`](https://docs.astral.sh/uv/) and [`Docker`](https://docs.docker.com/desktop/setup/install/windows-install/) installed.**

### Documentation:
> [RustFS](https://docs.rustfs.com/) ·
[boto3 S3 client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html) · [httpx](https://www.python-httpx.org/) · [python-dotenv](https://pypi.org/project/python-dotenv/)