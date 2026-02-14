from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class NodeCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Unique name/identifier of the node")
    label: str = Field(..., min_length=1, description="Primary label (e.g. Person, Company)")
    properties: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional attributes")

class NodeResponse(NodeCreate):
    id: str = Field(..., description="System ID")
    
    class Config:
        from_attributes = True
