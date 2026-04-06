# MLOps Homework – Sentiment Analysis API

## Overview

This project implements a production-ready sentiment analysis service using FastAPI.
The application performs inference using a pre-trained Sentence Transformer model and a logistic regression classifier.

The system follows basic MLOps principles:

* separation of code and model artifacts,
* automated model download,
* containerized deployment,
* automated testing.

---

## Features

* FastAPI web server
* `/predict` endpoint for sentiment analysis
* Input validation using Pydantic
* Automatic model download from Google Drive
* Unit tests using pytest
* Containerization with Docker and Docker Compose

---

## Project Structure

```
.
├── app.py
├── inference.py
├── api/
├── tests/
├── Dockerfile
├── docker-compose.yaml
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Model Handling

The model is not included in the repository due to size limitations.

On application startup:

1. The model archive is downloaded from Google Drive
2. The archive is extracted into the `models/` directory
3. The transformer and classifier are loaded into memory

This ensures:

* repository size remains below submission limits,
* reproducibility,
* clean separation of code and artifacts.

---

## Running Locally

### Install dependencies

```
uv sync
```

### Start the server

```
uv run uvicorn app:app --reload
```

### Test the API

```
Invoke-RestMethod `
  -Method Post `
  -Uri "http://127.0.0.1:8000/predict" `
  -ContentType "application/json" `
  -Body '{"text":"I love this product"}'
```

---

## API Endpoints

### Health check

```
GET /health
```

Response:

```
{"status": "ok"}
```

### Prediction

```
POST /predict
```

Request:

```
{
  "text": "I love this product"
}
```

Response:

```
{
  "prediction": "positive"
}
```

Possible outputs:

* negative
* neutral
* positive

---

## Testing

Run all tests:

```
uv run pytest -v
```

Tests cover:

* input validation,
* model loading,
* inference correctness,
* API responses.

---

## Docker

### Build and run

```
docker compose up --build
```

### Access API

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## Notes

* The model is downloaded at runtime, so the container requires internet access on first run.
* The `models/` directory and model artifacts are excluded from version control and Docker build context.

---

## Submission

The repository or archive should include:

* source code,
* Docker configuration,
* tests,
* dependency files.

Do not include:

* `.venv/`
* `models/`
* large model files or archives
