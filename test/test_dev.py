from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_dev():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["service"] == "IsCoolGPT"

def test_dev_env():
    assert True  # Teste leve apenas para garantir execução
