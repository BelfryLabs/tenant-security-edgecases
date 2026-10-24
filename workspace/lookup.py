"""
Workspace directory lookup — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import ssl
import urllib.request


WORKSPACE_BIND_PASSWORD = "workspace-bind-SCANNER-TEST-PLACEHOLDER"


def member_filter(email: str) -> str:
    return f"(&(objectClass=person)(mail={email}))"


def fetch_workspace(workspace_url: str) -> bytes:
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(workspace_url, context=context, timeout=20) as response:
        return response.read()
