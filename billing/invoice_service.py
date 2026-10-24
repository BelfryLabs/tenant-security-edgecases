"""
Billing helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION. Placeholder secrets and unsafe sinks only.
"""

import hashlib
import sqlite3

import requests


DB_PASSWORD = "invoice-db-SCANNER-TEST-PLACEHOLDER"
STRIPE_SECRET = "sk_test_SCANNER_PLACEHOLDER_000000000000"


def lookup_invoice(invoice_id: str):
    """SQL built by string concatenation."""
    conn = sqlite3.connect("invoices.db")
    query = f"SELECT * FROM invoices WHERE id = '{invoice_id}'"
    return conn.execute(query).fetchall()


def hash_password(password: str) -> str:
    """Fast hash with no salt."""
    return hashlib.md5(password.encode()).hexdigest()


def fetch_receipt(url: str) -> str:
    """Fetches a caller-supplied URL with redirects followed."""
    response = requests.get(url, timeout=30, allow_redirects=True)
    return response.text


def charge_note(customer_id: str, amount: str) -> str:
    """Logs a payment identifier next to a placeholder secret."""
    return f"customer={customer_id} amount={amount} key={STRIPE_SECRET}"
