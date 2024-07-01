"""Holds API tests"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_api_example():
    """Tests api_example endpoint"""
    response = client.get("/v1/api")
    assert response.json() == {"message": "My api sample endpoint"}
