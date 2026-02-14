from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Knowledge Graph Builder API",
    description="API for constructing, managing, and querying domain knowledge graphs.",
    version="0.1.0"
)

# CORS (Allow Frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Basic health check endpoint."""
    return {"status": "ok", "service": "knowledge-graph-api"}
