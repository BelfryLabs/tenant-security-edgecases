"""
Collection of dangerous patterns - INTENTIONALLY VULNERABLE for scanner testing.
DO NOT USE IN PRODUCTION.
"""

import os
import tempfile
import yaml
import pickle


def run_exec(user_input: str):
    """exec() with user input - arbitrary code execution."""
    exec(user_input)  # noqa: S102


def run_system_command(cmd: str):
    """os.system() with string concatenation - command injection."""
    os.system(cmd)  # noqa: S605


def load_yaml_untrusted(data: str):
    """yaml.load() without SafeLoader - arbitrary code execution."""
    return yaml.load(data, Loader=yaml.Loader)  # noqa: S506


def deserialize_untrusted(data: bytes):
    """Deserialization of untrusted data."""
    return pickle.loads(data)  # noqa: S301


def query_user(user_id: str):
    """SQL string concatenation - injection vulnerability."""
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return query  # Intentionally vulnerable


def read_file_unsafe(path: str):
    """Path traversal via unsanitized user input."""
    base = "/app/data"
    full_path = os.path.join(base, path)
    with open(full_path) as f:
        return f.read()


def create_temp_predictable():
    """Temporary files with predictable names."""
    temp_path = "/tmp/predictable_" + "user_data"
    with open(temp_path, "w") as f:
        f.write("data")
    return temp_path


def log_secrets_to_file(api_key: str, log_path: str = "/var/log/app.log"):
    """Logging secrets to file."""
    with open(log_path, "a") as f:
        f.write(f"API key in use: {api_key}\n")
