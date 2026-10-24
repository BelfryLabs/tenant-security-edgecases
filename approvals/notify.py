"""
Approval notifications — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import requests


TEAMS_WEBHOOK = "https://hooks.example.invalid/workflows/SCANNER/TEST/placeholder"


def post_decision(callback_url: str, body: dict) -> str:
    response = requests.post(callback_url, json=body, timeout=30, verify=False)
    return response.text


def render_decision(actor: str, note: str) -> str:
    return f"<section><h2>{actor}</h2><p>{note}</p></section>"
