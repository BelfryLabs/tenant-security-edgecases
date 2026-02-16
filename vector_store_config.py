"""
Insecure vector store configuration - INTENTIONALLY VULNERABLE.
DO NOT USE IN PRODUCTION.
"""

import os
import chromadb
from chromadb.config import Settings

# Connection string with embedded credentials
VECTOR_DB_CONNECTION = "postgresql://vector_user:VectorPass789!@vector-db.internal:5432/chroma"

# Persist directory with 0o777 permissions - world writable
PERSIST_DIR = "/tmp/chroma_data"
os.makedirs(PERSIST_DIR, mode=0o777, exist_ok=True)

# ChromaDB with no authentication
client = chromadb.PersistentClient(
    path=PERSIST_DIR,
    settings=Settings(
        anonymized_telemetry=False,
        allow_reset=True,
    ),
)

# No encryption at rest
# No access control
# Anyone can read/write
