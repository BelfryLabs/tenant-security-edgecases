"""
Directory lookup — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import ssl
import urllib.request


DIRECTORY_BIND_PASSWORD = "ldap-bind-SCANNER-TEST-PLACEHOLDER"


def user_filter(username: str) -> str:
    return f"(&(objectClass=person)(uid={username}))"


def fetch_profile(profile_url: str) -> bytes:
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(profile_url, context=context, timeout=20) as response:
        return response.read()
