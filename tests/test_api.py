from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_predict_returns_200_for_valid_input() -> None:
    response = client.post(
        "/predict",
        json={"text": "What a great MLOps lecture, I am very satisfied"},
    )

    assert response.status_code == 200


def test_predict_returns_valid_json_response() -> None:
    response = client.post(
        "/predict",
        json={"text": "What a great MLOps lecture, I am very satisfied"},
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert "prediction" in data
    assert isinstance(data["prediction"], str)
    assert data["prediction"] in {"negative", "neutral", "positive"}


def test_predict_rejects_empty_string() -> None:
    response = client.post(
        "/predict",
        json={"text": ""},
    )

    assert response.status_code == 422

    data = response.json()
    assert isinstance(data, dict)
    assert "detail" in data


def test_predict_rejects_whitespace_only_string() -> None:
    response = client.post(
        "/predict",
        json={"text": "   "},
    )

    assert response.status_code == 422

    data = response.json()
    assert isinstance(data, dict)
    assert "detail" in data


def test_predict_rejects_missing_text_field() -> None:
    response = client.post(
        "/predict",
        json={},
    )

    assert response.status_code == 422

    data = response.json()
    assert isinstance(data, dict)
    assert "detail" in data


def test_predict_rejects_non_string_text() -> None:
    response = client.post(
        "/predict",
        json={"text": 123},
    )

    assert response.status_code == 422

    data = response.json()
    assert isinstance(data, dict)
    assert "detail" in data
