"""
Evidence file helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import os
import zipfile


def read_evidence(relative_path: str) -> bytes:
    root = "/var/app/access-reviews"
    target = os.path.join(root, relative_path)
    with open(target, "rb") as handle:
        return handle.read()


def unpack_bundle(archive_path: str, dest: str) -> None:
    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(dest)


def share_link(bucket: str, key: str) -> dict:
    return {"Bucket": bucket, "Key": key, "ACL": "public-read"}
