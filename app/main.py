"""Minimal service for OCI deployment verification."""
from fastapi import FastAPI

app = FastAPI(title="Interaction Tree", docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
