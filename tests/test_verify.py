from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance
client = TestClient(app)

def test_verify_correct_answer():
    # Send a POST request to the /verify-answer endpoint with a correct answer
    response = client.post(
        "/verify-answer/",
        json={
            "question_id": 1,  # Replace with the actual ID of the question with answer "Onassis"
            "user_answer": "Copernicus"
        }
    )
    
    # Assert the response status code
    assert response.status_code == 200

    # Parse the response JSON
    data = response.json()

    # Assert the response structure and content
    assert "is_correct" in data
    assert "ai_response" in data

    # Validate the response values
    assert data["is_correct"] is True
    assert "Yes, Copernicus is the correct answer." in data["ai_response"]

def test_verify_incorrect_answer():
    # Send a POST request to the /verify-answer endpoint with an incorrect answer
    response = client.post(
        "/verify-answer/",
        json={
            "question_id": 1,  # Replace with the actual ID of the question with answer "Onassis"
            "user_answer": "Einstein"
        }
    )
    
    # Assert the response status code
    assert response.status_code == 200

    # Parse the response JSON
    data = response.json()

    # Assert the response structure and content
    assert "is_correct" in data
    assert "ai_response" in data

    # Validate the response values
    assert data["is_correct"] is False
    assert "Copernicus" in data["ai_response"]

def test_verify_nonexistent_question():
    # Send a POST request to the /verify-answer endpoint with a nonexistent question ID
    response = client.post(
        "/verify-answer/",
        json={
            "question_id": 9999999999,  # Assuming this ID does not exist
            "user_answer": "Some Answer"
        }
    )
    
    # Assert the response status code
    assert response.status_code == 404

    # Parse the response JSON
    data = response.json()

    # Assert the error message
    assert data["detail"] == "Question not found."