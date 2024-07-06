"""Holds API tests"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_api_example():
    """Tests api_example endpoint"""
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json() == {"message": "My api sample endpoint"}


def test_not_found():
    """Tests api_example endpoint"""
    response = client.get("/api/v1/not-found")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
