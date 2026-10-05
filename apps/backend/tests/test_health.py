from fastapi.testclient import TestClient

from ana.main import app


def test_health() -> None:
    response = TestClient(app).get("/backend/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
