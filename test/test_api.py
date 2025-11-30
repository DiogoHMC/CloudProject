# test/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["service"] == "IsCoolGPT"

def test_ask_minimal():
    payload = {
        "user_id": "u1",
        "topic": "Cloud infrestructure",
        "explanation_level": "beginner",
        "detail_level": "short"
    }
    r = client.post("/v1/ask", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "reply" in data
    assert "model" in data
