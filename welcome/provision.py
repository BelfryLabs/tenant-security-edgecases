"""
Provisioning job helpers — INTENTIONALLY VULNERABLE scanner fixtures.
DO NOT USE IN PRODUCTION.
"""

import pickle
import subprocess

import yaml


def load_plan(document: str):
    return yaml.load(document, Loader=yaml.Loader)  # noqa: S506


def restore_plan(blob: bytes):
    return pickle.loads(blob)  # noqa: S301


def apply_seed(script_path: str) -> str:
    completed = subprocess.run(
        f"bash {script_path}",
        shell=True,
        capture_output=True,
        text=True,
    )  # noqa: S602
    return completed.stdout
