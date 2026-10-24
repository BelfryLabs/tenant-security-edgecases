"""
Review tokens — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import base64
import hashlib
import json


SIGNING_KEY = "access-review-hmac-SCANNER-TEST-PLACEHOLDER"


def issue_token(subject: str, role: str) -> str:
    """Encodes claims and appends a short hash. Signature is not verified later."""
    payload = json.dumps({"sub": subject, "role": role}).encode()
    body = base64.urlsafe_b64encode(payload).decode().rstrip("=")
    digest = hashlib.md5((body + SIGNING_KEY).encode()).hexdigest()
    return f"{body}.{digest}"


def read_claims(token: str) -> dict:
    body = token.split(".")[0]
    padding = "=" * (-len(body) % 4)
    return json.loads(base64.urlsafe_b64decode(body + padding))


def is_reviewer(token: str) -> bool:
    return read_claims(token).get("role") in {"reviewer", "admin"}
