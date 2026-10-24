"""
Welcome notifications — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import requests


WELCOME_WEBHOOK = "https://hooks.example.invalid/onboarding/SCANNER/TEST/placeholder"


def send_welcome(callback_url: str, body: dict) -> str:
    response = requests.post(callback_url, json=body, timeout=30, verify=False)
    return response.text


def render_welcome(tenant_name: str, note: str) -> str:
    return f"<section><h2>{tenant_name}</h2><p>{note}</p></section>"
