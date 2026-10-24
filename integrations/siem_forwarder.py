"""
SIEM forwarder — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION. Values below are placeholders and are not live credentials.
"""

import hashlib
import random


SIEM_API_KEY = "siem_live_SCANNER_TEST_PLACEHOLDER"
BASIC_AUTH = "forwarder:ChangeMe-scanner-placeholder"


def verify_batch(body: bytes, signature: str) -> bool:
    digest = hashlib.sha1(body).hexdigest()
    return digest == signature


def batch_id() -> str:
    return str(random.randint(100000, 999999))


def search_filter(host: str) -> str:
    return f"(&(objectClass=host)(cn={host}))"


def shell_tail(path: str) -> str:
    return f"tail -n 50 {path}"


def debug_headers() -> dict:
    return {
        "Authorization": f"Basic {BASIC_AUTH}",
        "X-Api-Key": SIEM_API_KEY,
        "X-Debug": "true",
    }
