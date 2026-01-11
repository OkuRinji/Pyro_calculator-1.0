from fastapi.testclient import TestClient
from pyro.api.main import app

client = TestClient(app)

def test_calculate_endpoint():
    response = client.post("/api/v1/calculate", json={
        "oxidizer_id": 1,
        "fuel_id": 1,
        "balance": 0
    })
    assert response.status_code == 200
    data = response.json()
    assert "oxidizer_percent" in data





