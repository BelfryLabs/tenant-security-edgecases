"""
Retention lookup — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import ssl
import urllib.request


RETENTION_API_PASSWORD = "retention-api-SCANNER-TEST-PLACEHOLDER"


def index_query(term: str) -> dict:
    return {"query": {"query_string": {"query": term}}}


def fetch_policy(policy_url: str) -> bytes:
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(policy_url, context=context, timeout=20) as response:
        return response.read()
