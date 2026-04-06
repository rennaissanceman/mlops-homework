# MLOps Lab 1 — Sentiment Analysis API - Homework

## 📌 Overview

This project is a **production-ready FastAPI application** for sentiment analysis.

It exposes a REST API that classifies text into:

* `negative`
* `neutral`
* `positive`

The model is automatically downloaded on first run and cached locally.

---

## ⚙️ Requirements

* Python **3.12+**
* [uv](https://www.google.com/search?q=uv+python+package+manager+installation)
* Docker (optional)

---

## 🚀 Run locally (recommended)

### 1. Install dependencies

```bash
uv sync
```

### 2. Run application

```bash
uv run uvicorn app:app --reload
```

### 3. Open API

* Swagger UI: http://localhost:8000/docs
* Health check:

```bash
curl http://localhost:8000/health
```

---

## 🐳 Run with Docker

### Build and run

```bash
docker compose up --build
```

### Open API

* http://localhost:8000/docs

---

## 🧠 Model

On first run, the application:

1. Downloads the model archive from Google Drive
2. Extracts it into the `models/` directory
3. Loads:

   * Sentence Transformer encoder
   * Classification model (`joblib`)

Internet is required only for the first run.

---

## 📡 API

### Health check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Predict sentiment

```http
POST /predict
```

Request:

```json
{
  "text": "I love this product"
}
```

Response:

```json
{
  "prediction": "positive"
}
```

---

## 🧪 Tests

Run all tests:

```bash
uv run pytest tests -vv
```

Covers:

* input validation
* API responses
* model loading
* inference correctness

---

## 🧹 Code quality

Pre-commit hooks:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

Includes:

* Ruff (lint + format)
* mypy (type checking)

---

## 📁 Project structure

```
.
├── app.py
├── inference.py
├── api/
│   └── models/
├── tests/
├── models/
├── pyproject.toml
├── docker-compose.yaml
├── Dockerfile
```

---

## ✅ Features

* FastAPI REST API
* Automatic model download
* Input validation (Pydantic)
* Unit & integration tests (pytest)
* Static typing (mypy)
* Code linting (ruff)
* Containerized with Docker

---

## 📌 Notes

* The model is stored locally after first run
* No GPU is required (CPU version of PyTorch is used)
* Designed for reproducibility using `uv`
