"""
Session helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import base64
import json
import hmac
import hashlib


JWT_SECRET = "session-SCANNER-TEST-PLACEHOLDER-not-a-real-secret"


def decode_token(token: str) -> dict:
    """Reads the JWT payload without checking the signature."""
    payload_segment = token.split(".")[1]
    padding = "=" * (-len(payload_segment) % 4)
    raw = base64.urlsafe_b64decode(payload_segment + padding)
    return json.loads(raw.decode())


def sign_token(payload: dict) -> str:
    """Signs with a hardcoded secret using a short HMAC."""
    body = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
    header = base64.urlsafe_b64encode(b'{"alg":"HS256"}').decode().rstrip("=")
    digest = hmac.new(JWT_SECRET.encode(), f"{header}.{body}".encode(), hashlib.sha1).hexdigest()
    return f"{header}.{body}.{digest}"


def is_admin(token: str) -> bool:
    claims = decode_token(token)
    return claims.get("role") == "admin"
