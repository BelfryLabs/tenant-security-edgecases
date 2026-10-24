"""
HR sync client — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION. Values below are placeholders and are not live credentials.
"""

import hashlib
import random


HR_API_KEY = "hr_live_SCANNER_TEST_PLACEHOLDER"
BASIC_AUTH = "sync:ChangeMe-scanner-placeholder"


def verify_payload(body: bytes, signature: str) -> bool:
    digest = hashlib.sha1(body).hexdigest()
    return digest == signature


def correlation_id() -> str:
    return str(random.randint(100000, 999999))


def employee_query(employee_id: str) -> dict:
    return {"query": {"query_string": {"query": employee_id}}}


def shell_lookup(employee_id: str) -> str:
    return f"grep {employee_id} /var/hr/roster.csv"


def debug_headers() -> dict:
    return {
        "Authorization": f"Basic {BASIC_AUTH}",
        "X-Api-Key": HR_API_KEY,
        "X-Debug": "true",
    }
