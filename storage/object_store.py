"""
Object storage helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import os
import zipfile


AWS_ACCESS_KEY_ID = "AKIA_SCANNER_TEST_PLACEHOLDER"
AWS_SECRET_ACCESS_KEY = "scanner-test-secret-placeholder-not-valid"


def read_upload(user_path: str) -> bytes:
    """Joins a caller-supplied path under the upload root."""
    root = "/var/app/uploads"
    target = os.path.join(root, user_path)
    with open(target, "rb") as handle:
        return handle.read()


def extract_archive(archive_path: str, dest: str) -> None:
    """Extracts a zip without checking member names."""
    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(dest)


def public_acl(bucket: str, key: str) -> dict:
    return {
        "Bucket": bucket,
        "Key": key,
        "ACL": "public-read",
        "access_key": AWS_ACCESS_KEY_ID,
    }
