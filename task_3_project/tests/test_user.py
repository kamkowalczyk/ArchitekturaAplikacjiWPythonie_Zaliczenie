import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_create_user(db_session):
    """User creation test"""
    response = client.post("/api/v1/users/", json={"username": "testuser", "email": "testuser@example.com", "hashed_password": "password123"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_read_user(db_session):
    """User reading test"""
    response = client.post("/api/v1/users/", json={"username": "testuser2", "email": "testuser2@example.com", "hashed_password": "password123"})
    user_id = response.json()["id"]
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser2"