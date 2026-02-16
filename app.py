"""
FastAPI app with intentional security anti-patterns for static scanner testing.
DO NOT USE IN PRODUCTION - FOR SCANNER TRIGGER TESTING ONLY.
"""

import subprocess
import pickle
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Hardcoded secrets - INTENTIONALLY VULNERABLE (scanner test placeholders)
OPENAI_API_KEY = "sk-proj-SCANNER-TEST-PLACEHOLDER-abc123def456ghi789"
DATABASE_URL = "postgresql://admin:SCANNER_TEST_PASSWORD@prod-db.internal:5432/app"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYSCANNER_TEST_KEY"
STRIPE_SECRET_KEY = "sk_live_SCANNER_TEST_PLACEHOLDER_NOT_REAL_KEY"

app = FastAPI(title="Vulnerable Demo API")

# CORS with allow_origins=["*"] - overly permissive
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Direct API key logging - secrets in logs
print(f"Using API key: {OPENAI_API_KEY}")


@app.get("/")
async def root():
    return {"message": "Vulnerable API - scanner test"}


@app.post("/eval")
async def eval_endpoint(request: Request):
    """Dangerous: eval() on user input - arbitrary code execution."""
    body = await request.json()
    user_input = body.get("expression", "")
    result = eval(user_input)  # noqa: S307
    return {"result": str(result)}


@app.post("/exec")
async def exec_endpoint(request: Request):
    """Dangerous: exec() on user input."""
    body = await request.json()
    user_input = body.get("code", "")
    exec(user_input)  # noqa: S102
    return {"status": "executed"}


@app.post("/run")
async def run_command(request: Request):
    """Dangerous: subprocess.Popen with shell=True and user input."""
    body = await request.json()
    cmd = body.get("command", "echo hello")
    proc = subprocess.Popen(cmd, shell=True)  # noqa: S602
    proc.wait()
    return {"status": "completed"}


@app.post("/unpickle")
async def unpickle_endpoint(request: Request):
    """Dangerous: pickle.loads on user-provided data - arbitrary code execution."""
    body = await request.body()
    obj = pickle.loads(body)  # noqa: S301
    return {"unpickled": str(obj)}


@app.get("/config")
async def get_config():
    """Leaks credentials in response - no output filtering."""
    return {
        "database_url": DATABASE_URL,
        "aws_key": AWS_SECRET_ACCESS_KEY,
        "stripe_key": STRIPE_SECRET_KEY,
    }
