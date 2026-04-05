from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_create_meeting_ok():
    payload = {"title": "Planning", "date": "2026-03-10", "owner": "Jorge"}
    r = client.post("/meetings", json=payload)
    assert r.status_code == 201


def test_dashboard_summary():
    r = client.get("/dashboard/summary")
    assert r.status_code == 200
    data = r.json()
    assert "total_meetings" in data
    assert "total_action_items" in data
