#test_api.py
# Import TestClient to test FastAPI endpoints without running a real server
from fastapi.testclient import TestClient  # Part of fastapi testing utilities

# Import the FastAPI app instance
from app.api.main import app  # Local import of the API application


# Create a TestClient instance using the FastAPI app
client = TestClient(app)


# Define a test function for the /health endpoint
def test_health_check():
    # Send a GET request to /health
    response = client.get("/health")

    # Assert that the HTTP status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the JSON response contains the expected status
    assert response.json() == {"status": "OK"}


# Define a test function for the /decision endpoint
def test_decision_endpoint():
    # Build a sample application payload
    payload = {
        "credit_score": 720,
        "income": 90000,
        "utilization": 20,
        "delinquency_flag": False,
        "requested_amount": 7000,
    }

    # Send a POST request to /decision with the payload as JSON
    response = client.post("/decision", json=payload)

    # Assert that the HTTP status code is 200 (OK)
    assert response.status_code == 200

    # Parse the JSON response body
    data = response.json()

    # Assert that the decision field exists in the response
    assert "decision" in data

    # Assert that the decision is APPROVE for this payload
    assert data["decision"] == "APPROVE"
