"""
Approval policy helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import pickle
import subprocess

import yaml


def load_policy(document: str):
    return yaml.load(document, Loader=yaml.Loader)  # noqa: S506


def restore_decision(blob: bytes):
    return pickle.loads(blob)  # noqa: S301


def export_audit(path: str) -> str:
    completed = subprocess.run(
        f"cat {path}",
        shell=True,
        capture_output=True,
        text=True,
    )  # noqa: S602
    return completed.stdout
