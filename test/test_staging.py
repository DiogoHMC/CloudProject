import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_staging():
    r = client.get("/")
    assert r.status_code == 200

def test_api_key_present():
    # Garante que a key está configurada no ambiente do Render Staging
    key = os.getenv("GEMINI_API_KEY")
    assert key is not None
    assert len(key) > 5
