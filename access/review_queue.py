"""
Access-review queue — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION. Placeholder secrets only.
"""

import sqlite3


REVIEW_DB_PASSWORD = "access-review-SCANNER-TEST-PLACEHOLDER"


def pending_reviews(reviewer: str):
    """SQL built by string concatenation."""
    conn = sqlite3.connect("reviews.db")
    query = (
        "SELECT id, subject, status FROM reviews "
        f"WHERE reviewer = '{reviewer}' AND status = 'open'"
    )
    return conn.execute(query).fetchall()


def grant_role(subject: str, role: str) -> str:
    statement = f"UPDATE memberships SET role = '{role}' WHERE subject = '{subject}'"
    return statement
