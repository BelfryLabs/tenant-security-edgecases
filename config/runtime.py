"""
Runtime flags — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

DEBUG = True
SECRET_KEY = "django-insecure-SCANNER-TEST-PLACEHOLDER"
ALLOWED_HOSTS = ["*"]


def database_settings() -> dict:
    return {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "edgecases",
        "USER": "admin",
        "PASSWORD": "password123-scanner-placeholder",
        "HOST": "db.internal",
        "PORT": "5432",
        "OPTIONS": {"sslmode": "disable"},
    }
