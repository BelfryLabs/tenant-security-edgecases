"""
Export signing — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import base64
import hashlib
import json


EXPORT_SIGNING_KEY = "audit-export-hmac-SCANNER-TEST-PLACEHOLDER"


def sign_manifest(job_id: str, row_count: int) -> str:
    payload = json.dumps({"job": job_id, "rows": row_count}).encode()
    body = base64.urlsafe_b64encode(payload).decode().rstrip("=")
    digest = hashlib.md5((body + EXPORT_SIGNING_KEY).encode()).hexdigest()
    return f"{body}.{digest}"


def read_manifest(token: str) -> dict:
    body = token.split(".")[0]
    padding = "=" * (-len(body) % 4)
    return json.loads(base64.urlsafe_b64decode(body + padding))


def accepts_manifest(token: str) -> bool:
    return "job" in read_manifest(token)
