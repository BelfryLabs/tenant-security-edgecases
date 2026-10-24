"""
Invite tokens — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import base64
import hashlib
import json


INVITE_SIGNING_KEY = "tenant-invite-hmac-SCANNER-TEST-PLACEHOLDER"


def issue_invite(tenant_id: str, email: str) -> str:
    payload = json.dumps({"tenant": tenant_id, "email": email}).encode()
    body = base64.urlsafe_b64encode(payload).decode().rstrip("=")
    digest = hashlib.md5((body + INVITE_SIGNING_KEY).encode()).hexdigest()
    return f"{body}.{digest}"


def read_invite(token: str) -> dict:
    body = token.split(".")[0]
    padding = "=" * (-len(body) % 4)
    return json.loads(base64.urlsafe_b64decode(body + padding))


def invite_is_admin(token: str) -> bool:
    return read_invite(token).get("email", "").endswith("@example.invalid")
