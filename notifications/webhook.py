"""
Outbound webhook helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import ssl
import urllib.request


SLACK_WEBHOOK = "https://hooks.example.invalid/services/SCANNER/TEST/placeholder"


def post_event(callback_url: str, body: bytes) -> int:
    """Posts to a caller-supplied URL and disables TLS verification."""
    context = ssl._create_unverified_context()
    request = urllib.request.Request(callback_url, data=body, method="POST")
    with urllib.request.urlopen(request, context=context, timeout=20) as response:
        return response.status


def render_alert(title: str, detail: str) -> str:
    """Builds HTML from unsanitized fields."""
    return f"<div class='alert'><h1>{title}</h1><p>{detail}</p></div>"
