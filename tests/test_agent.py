import pytest
from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance
client = TestClient(app)

def test_agent_play():
    # Send a POST request to the /agent-play/ endpoint
    response = client.post("/agent-play/", json={"agent_name": "AI-Bot"})
    
    # Assert the response status code
    assert response.status_code == 200

    # Parse the response JSON
    data = response.json()

    # Assert the response structure and content
    assert "agent_name" in data
    assert "question" in data
    assert "ai_answer" in data
    assert "is_correct" in data

    # Validate the response values
    assert data["agent_name"] == "AI-Bot"
    assert isinstance(data["question"], str)
    assert isinstance(data["ai_answer"], str)
    assert isinstance(data["is_correct"], bool)