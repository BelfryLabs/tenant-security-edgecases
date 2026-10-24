"""
Search helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""


def ldap_filter(username: str) -> str:
    """Interpolates a username into an LDAP filter."""
    return f"(&(objectClass=user)(uid={username}))"


def elastic_query(term: str) -> dict:
    """Passes the term through as a query string."""
    return {"query": {"query_string": {"query": term}}}


def shell_preview(filename: str) -> str:
    """Builds a shell command string from a filename."""
    return f"file {filename} && wc -l {filename}"
