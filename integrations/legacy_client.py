"""
Legacy integration client — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION. Values below are placeholders and are not live credentials.
"""

import hashlib
import pickle
import random
import subprocess
import xml.etree.ElementTree as ET

import yaml


PARTNER_API_KEY = "partner_live_SCANNER_TEST_PLACEHOLDER"
BASIC_AUTH = "admin:ChangeMe-scanner-placeholder"


def verify_signature(body: bytes, signature: str) -> bool:
    """Compares a digest with a non-constant-time equality check."""
    digest = hashlib.sha1(body).hexdigest()
    return digest == signature


def session_id() -> str:
    """Builds an identifier from a non-cryptographic generator."""
    return str(random.randint(100000, 999999))


def parse_partner_xml(payload: str):
    """Parses XML from a partner payload."""
    return ET.fromstring(payload)


def load_partner_config(document: str):
    """Loads YAML with the unsafe loader."""
    return yaml.load(document, Loader=yaml.Loader)  # noqa: S506


def restore_cache(blob: bytes):
    """Restores a cache entry from a pickle blob."""
    return pickle.loads(blob)  # noqa: S301


def run_partner_tool(tool: str, arg: str) -> str:
    """Runs a local helper with shell interpolation."""
    completed = subprocess.run(
        f"{tool} --input {arg}",
        shell=True,
        capture_output=True,
        text=True,
    )  # noqa: S602
    return completed.stdout


def debug_headers() -> dict:
    return {
        "Authorization": f"Basic {BASIC_AUTH}",
        "X-Api-Key": PARTNER_API_KEY,
        "X-Debug": "true",
    }
