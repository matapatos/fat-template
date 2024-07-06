"""Holds pages tests"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_homepage():
    """Tests accessing homepage"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_page_not_found():
    """Tests accessing a non-existent page"""
    response = client.get("/not-found/page")
    assert response.status_code == 404
    assert response.headers["content-type"] == "text/html; charset=utf-8"
