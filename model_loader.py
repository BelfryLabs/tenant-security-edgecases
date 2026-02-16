"""
Unsafe model loading - INTENTIONALLY VULNERABLE for static scanner testing.
DO NOT USE IN PRODUCTION.
"""

import os
import pickle
import urllib.request
import ssl

import torch


def load_pickle_from_path(path: str):
    """Load pickle file from untrusted source - arbitrary code execution."""
    with open(path, "rb") as f:
        return pickle.load(f)  # noqa: S301


def load_model_weights(path: str):
    """Load model weights without signature verification or hash checking."""
    return torch.load(path, weights_only=False)  # noqa: S301


def download_model_from_url(url: str, dest: str):
    """Download model from arbitrary URL without TLS verification."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    urllib.request.urlretrieve(url, dest, context=ctx)


def load_untrusted_model(url: str):
    """Full pipeline: download from untrusted URL, load without verification."""
    tmp_path = "/tmp/downloaded_model.pt"
    download_model_from_url(url, tmp_path)
    model = load_model_weights(tmp_path)
    os.remove(tmp_path)
    return model
