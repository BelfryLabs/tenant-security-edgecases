"""
Onboarding file helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import os
import zipfile


def read_packet(relative_path: str) -> bytes:
    root = "/var/app/onboarding"
    target = os.path.join(root, relative_path)
    with open(target, "rb") as handle:
        return handle.read()


def unpack_packet(archive_path: str, dest: str) -> None:
    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(dest)


def publish_logo(bucket: str, key: str) -> dict:
    return {"Bucket": bucket, "Key": key, "ACL": "public-read"}
