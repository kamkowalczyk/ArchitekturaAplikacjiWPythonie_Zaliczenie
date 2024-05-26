import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/v1/users/", json={"username": "testuser", "email": "testuser@example.com", "hashed_password": "password123"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
