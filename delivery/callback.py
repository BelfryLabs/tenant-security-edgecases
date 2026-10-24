"""
Export delivery — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import requests


DELIVERY_WEBHOOK = "https://hooks.example.invalid/audit/SCANNER/TEST/placeholder"


def deliver(callback_url: str, body: dict) -> str:
    response = requests.post(callback_url, json=body, timeout=30, verify=False)
    return response.text


def render_status(job_name: str, detail: str) -> str:
    return f"<article><h2>{job_name}</h2><p>{detail}</p></article>"
