from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_returns_positive_for_valid_text() -> None:
    response = client.post("/predict", json={"text": "This lecture was great"})

    assert response.status_code == 200
    assert response.json() == {"prediction": "positive"}


def test_predict_rejects_empty_text() -> None:
    response = client.post("/predict", json={"text": ""})

    assert response.status_code == 422
    assert "detail" in response.json()


def test_predict_rejects_whitespace_only_text() -> None:
    response = client.post("/predict", json={"text": "   "})

    assert response.status_code == 422
    assert "detail" in response.json()


def test_predict_rejects_missing_text_field() -> None:
    response = client.post("/predict", json={})

    assert response.status_code == 422
    assert "detail" in response.json()


def test_predict_rejects_non_string_text() -> None:
    response = client.post("/predict", json={"text": 123})

    assert response.status_code == 422
    assert "detail" in response.json()
