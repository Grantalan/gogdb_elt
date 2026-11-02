"""Settings and clients for the pipeline. Values come from .env."""

import os

import boto3
import httpx
from botocore.client import BaseClient
from botocore.config import Config
from dotenv import load_dotenv

load_dotenv()

# Source: GOG DB
API_BASE_URL = os.environ["API_BASE_URL"]

# Raw landing zone: RustFS / S3
S3_ENDPOINT_URL = os.environ["S3_ENDPOINT_URL"]
S3_ACCESS_KEY = os.environ["S3_ACCESS_KEY"]
S3_SECRET_KEY = os.environ["S3_SECRET_KEY"]
S3_REGION = os.getenv("S3_REGION", "us-east-1")
S3_BUCKET = os.environ["S3_BUCKET"]


def get_s3_client() -> BaseClient:
    """boto3 client for RustFS."""
    return boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT_URL,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
        region_name=S3_REGION,
        config=Config(s3={"addressing_style": "path"}),  # RustFS needs path-style URLs
    )


def get_http_client() -> httpx.Client:
    """httpx client for GOG DB."""
    return httpx.Client(
        base_url=API_BASE_URL,
        headers={"User-Agent": "gogdb-pipeline (student data engineering project)"},
        timeout=30,
        follow_redirects=True,
    )
