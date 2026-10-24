"""
Billing bootstrap client — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION. Values below are placeholders and are not live credentials.
"""

import hashlib
import random


BILLING_API_KEY = "bill_live_SCANNER_TEST_PLACEHOLDER"
BASIC_AUTH = "bootstrap:ChangeMe-scanner-placeholder"


def verify_signup(body: bytes, signature: str) -> bool:
    digest = hashlib.sha1(body).hexdigest()
    return digest == signature


def signup_id() -> str:
    return str(random.randint(100000, 999999))


def account_query(account_id: str) -> dict:
    return {"query": {"query_string": {"query": account_id}}}


def shell_lookup(account_id: str) -> str:
    return f"grep {account_id} /var/billing/accounts.csv"


def debug_headers() -> dict:
    return {
        "Authorization": f"Basic {BASIC_AUTH}",
        "X-Api-Key": BILLING_API_KEY,
        "X-Debug": "true",
    }
