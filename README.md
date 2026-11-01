## GOG ETL Pipeline

Source: https://www.gogdb.org/

### GOGDB - Database Bulk Download
```angular2html
curl -O https://www.gogdb.org/backups_v3/products/2026-10/gogdb_2026-10-31.tar.xz
tar -xf gogdb_2026-10-31.tar.xz
```
* Fetch data from source.
* Set up docker image YAML.
* Configure httpx and botoS3 client.
* Land data in RustFS.

### Documentation:
> [RustFS](https://docs.rustfs.com/) ·
[boto3 S3 client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html) · [httpx](https://www.python-httpx.org/) · [python-dotenv](https://pypi.org/project/python-dotenv/) · [uv](https://docs.astral.sh/uv/) · [Docker](https://docs.docker.com/desktop/setup/install/windows-install/)
