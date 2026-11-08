## GOG ETL Pipeline

Source: https://www.gogdb.org/

### GOGDB - Bulk Download (~1.1 GB)
```bash
mkdir -p data/sample && rm -rf data/sample/products
curl -s https://www.gogdb.org/backups_v3/products/$(curl -s https://www.gogdb.org/backups_v3/products/filelist.txt | tail -1) | tar -xJ -C data/sample
```
* Fetch data from source.
* Set up docker image YAML.
* Configure httpx and botoS3 client.
* Land data in RustFS.

### Run the pipeline
1. `cp .env.example .env` fill in variables:
   - `API_BASE_URL=https://www.gogdb.org`
   - `S3_ENDPOINT_URL=http://localhost:9020`
   - `S3_ACCESS_KEY=`: choose password
   - `S3_SECRET_KEY=`: choose password
   - `S3_REGION=us-east-1` 
   - `S3_BUCKET=gogdb-raw`
2. `docker compose up -d`
3. `uv sync`
4. `uv run gogdb-pipeline`

### Documentation:
> [RustFS](https://docs.rustfs.com/) ·
[boto3 S3 client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html) · [httpx](https://www.python-httpx.org/) · [python-dotenv](https://pypi.org/project/python-dotenv/) · [uv](https://docs.astral.sh/uv/) · [Docker](https://docs.docker.com/desktop/setup/install/windows-install/)
