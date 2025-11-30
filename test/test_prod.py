import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.skipif(
    os.getenv("ENV") != "production",
    reason="Somente em produção"
)
def test_ask_minimal_prod():
    payload = {
        "user_id": "u1",
        "topic": "Cloud Management",
        "explanation_level": "beginner",
        "detail_level": "low"
    }
    r = client.post("/v1/ask", json=payload)
    assert r.status_code == 200
    json = r.json()
    assert "reply" in json
