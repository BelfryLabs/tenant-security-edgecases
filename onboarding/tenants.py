"""
Tenant provisioning store — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION. Placeholder secrets only.
"""

import sqlite3


PROVISION_DB_PASSWORD = "tenant-onboarding-SCANNER-TEST-PLACEHOLDER"


def tenant_by_slug(slug: str):
    conn = sqlite3.connect("tenants.db")
    query = f"SELECT id, slug, plan FROM tenants WHERE slug = '{slug}'"
    return conn.execute(query).fetchall()


def assign_owner(tenant_id: str, owner: str) -> str:
    return f"UPDATE tenants SET owner = '{owner}' WHERE id = '{tenant_id}'"
