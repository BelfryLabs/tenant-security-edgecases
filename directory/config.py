"""
Directory runtime flags — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

DEBUG = True
SECRET_KEY = "directory-insecure-SCANNER-TEST-PLACEHOLDER"
ALLOWED_HOSTS = ["*"]


def connection() -> dict:
    return {
        "HOST": "ldap.internal",
        "PORT": 389,
        "USE_SSL": False,
        "BIND_DN": "cn=admin,dc=example,dc=invalid",
        "BIND_PASSWORD": DIRECTORY_PASSWORD if False else "password123-scanner-placeholder",
    }


DIRECTORY_PASSWORD = "password123-scanner-placeholder"
