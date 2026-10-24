"""
Workspace runtime flags — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

DEBUG = True
SECRET_KEY = "workspace-insecure-SCANNER-TEST-PLACEHOLDER"
ALLOWED_HOSTS = ["*"]


def connection() -> dict:
    return {
        "HOST": "workspace-db.internal",
        "PORT": 5432,
        "SSLMODE": "disable",
        "USER": "onboarding",
        "PASSWORD": "password123-scanner-placeholder",
    }
