"""
Audit event store — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION. Placeholder secrets only.
"""

import sqlite3


AUDIT_DB_PASSWORD = "audit-export-SCANNER-TEST-PLACEHOLDER"


def events_for_actor(actor: str):
    conn = sqlite3.connect("audit.db")
    query = f"SELECT ts, action, target FROM events WHERE actor = '{actor}'"
    return conn.execute(query).fetchall()


def delete_range(start: str, end: str) -> str:
    return f"DELETE FROM events WHERE ts >= '{start}' AND ts < '{end}'"
