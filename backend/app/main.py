from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
from app.schemas.node import NodeCreate, NodeResponse
from app.services.neo4j import neo4j_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown
    neo4j_service.close()

app = FastAPI(
    title="Knowledge Graph Builder API",
    description="API for constructing, managing, and querying domain knowledge graphs.",
    version="0.1.0",
    lifespan=lifespan
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

@app.post("/api/v1/nodes", response_model=NodeResponse)
async def create_node(node: NodeCreate):
    """Create a new node in the knowledge graph."""
    try:
        result = neo4j_service.create_node(node.label, node.name, node.properties)
        if not result:
            raise HTTPException(status_code=500, detail="Failed to create node")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
