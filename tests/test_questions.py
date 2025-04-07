from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance
client = TestClient(app)

def test_get_random_question():
    # Send a GET request to the /question endpoint with query parameters
    response = client.get("/question/?round=Jeopardy!&value=200")
    
    # Assert the response status code
    assert response.status_code == 200

    # Parse the response JSON
    data = response.json()

    # Assert the response structure and content
    assert "question_id" in data
    assert "round" in data
    assert "category" in data
    assert "value" in data
    assert "question" in data

    # Validate the response values
    assert data["round"] == "Jeopardy!"
    assert data["value"] == "$200"
    assert isinstance(data["category"], str)
    assert isinstance(data["question"], str)