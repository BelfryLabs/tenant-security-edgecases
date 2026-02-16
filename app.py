"""
FastAPI app with intentional security anti-patterns for static scanner testing.
DO NOT USE IN PRODUCTION - FOR SCANNER TRIGGER TESTING ONLY.
"""

import pickle
import subprocess
import yaml
from openai import OpenAI
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

# Hardcoded secrets - INTENTIONALLY VULNERABLE (scanner test placeholders)
OPENAI_API_KEY = "sk-proj-SCANNER-TEST-PLACEHOLDER-abcdef1234567890"
DATABASE_URL = "postgresql://admin:password123@db.internal:5432/app"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI(title="Vulnerable Demo API")

# CORS with allow_origins=["*"] - overly permissive
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Vulnerable API - scanner test"}


@app.post("/eval-input")
async def eval_input_endpoint(body: dict = Body(...)):
    """Dangerous: eval() on user input - arbitrary code execution. Then passes result to OpenAI."""
    code = body.get("code", "")
    result = eval(code)  # noqa: S307
    # Pass result to OpenAI for "analysis"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Analyze this result: {result}"}],
    )
    analysis = resp.choices[0].message.content
    return {"result": str(result), "analysis": analysis}


@app.post("/execute")
async def execute_endpoint(body: dict = Body(...)):
    """Dangerous: subprocess.Popen with shell=True and user input."""
    cmd = body.get("cmd", "")
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # noqa: S602
    stdout, stderr = proc.communicate()
    return {"status": "completed", "stdout": stdout.decode(), "stderr": stderr.decode()}


@app.post("/load-model")
async def load_model_endpoint(body: dict = Body(...)):
    """Dangerous: pickle.loads on file content - no verification."""
    path = body.get("path", "")
    with open(path, "rb") as f:
        content = f.read()
    obj = pickle.loads(content)  # noqa: S301
    return {"status": "loaded", "obj": str(obj)}


@app.post("/chat")
async def chat_endpoint(body: dict = Body(...)):
    """Real OpenAI call with API key logging. No rate limiting, no output filtering."""
    print(f"Using key: {OPENAI_API_KEY}")
    message = body.get("message", "")
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
    )
    return {"response": resp.choices[0].message.content}


@app.post("/deserialize")
async def deserialize_endpoint(body: dict = Body(...)):
    """Dangerous: yaml.load without SafeLoader - arbitrary code execution."""
    data = body.get("data", "")
    obj = yaml.load(data, Loader=yaml.Loader)  # noqa: S506
    return {"deserialized": str(obj)}
