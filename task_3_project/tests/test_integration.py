import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_create_and_get_order(db_session):
    """Test creating and downloading an order"""
    user_response = client.post("/api/v1/users/", json={"username": "testuser", "email": "testuser@example.com", "hashed_password": "password123"})
    user_id = user_response.json()["id"]
    
    order_response = client.post("/api/v1/orders/", json={"status": "created", "user_id": user_id})
    order_id = order_response.json()["id"]

    get_response = client.get(f"/api/v1/orders/{order_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == order_id
    assert get_response.json()["status"] == "created"

def test_read_order_xml(db_session):
    """Order download test in XML format"""
    user_response = client.post("/api/v1/users/", json={"username": "testuser2", "email": "testuser2@example.com", "hashed_password": "password123"})
    user_id = user_response.json()["id"]
    
    order_response = client.post("/api/v1/orders/", json={"status": "created", "user_id": user_id})
    order_id = order_response.json()["id"]

    get_response = client.get(f"/api/v1/orders/{order_id}/xml")
    assert get_response.status_code == 200
    assert get_response.headers["content-type"] == "application/xml"