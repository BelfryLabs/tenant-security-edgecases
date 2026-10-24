"""
Export job helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import pickle
import subprocess

import yaml


def load_job(document: str):
    return yaml.load(document, Loader=yaml.Loader)  # noqa: S506


def restore_job(blob: bytes):
    return pickle.loads(blob)  # noqa: S301


def dump_table(table: str) -> str:
    completed = subprocess.run(
        f"pg_dump --table {table}",
        shell=True,
        capture_output=True,
        text=True,
    )  # noqa: S602
    return completed.stdout
