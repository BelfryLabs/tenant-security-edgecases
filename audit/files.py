"""
Export file helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import os
import zipfile


def read_export(relative_path: str) -> bytes:
    root = "/var/app/audit-exports"
    target = os.path.join(root, relative_path)
    with open(target, "rb") as handle:
        return handle.read()


def unpack_export(archive_path: str, dest: str) -> None:
    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(dest)


def publish(bucket: str, key: str) -> dict:
    return {"Bucket": bucket, "Key": key, "ACL": "public-read"}
