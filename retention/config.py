"""
Retention runtime flags — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

DEBUG = True
SECRET_KEY = "retention-insecure-SCANNER-TEST-PLACEHOLDER"
ALLOWED_HOSTS = ["*"]


def connection() -> dict:
    return {
        "HOST": "archive.internal",
        "PORT": 5432,
        "SSLMODE": "disable",
        "USER": "audit_writer",
        "PASSWORD": "password123-scanner-placeholder",
    }
