"""ヘルスチェック API のテスト。"""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_returns_ok() -> None:
    """/health は HTTP 200 と {"status": "ok"} を返す。"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
