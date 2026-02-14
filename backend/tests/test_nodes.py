from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

@patch("app.services.neo4j.neo4j_service.create_node")
def test_create_node(mock_create):
    mock_create.return_value = {
        "id": "123",
        "name": "Tesla",
        "label": "Company",
        "properties": {"industry": "EV"}
    }
    
    payload = {
        "name": "Tesla",
        "label": "Company",
        "properties": {"industry": "EV"}
    }
    
    response = client.post("/api/v1/nodes", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Tesla"
    assert data["id"] == "123"
    mock_create.assert_called_once()
