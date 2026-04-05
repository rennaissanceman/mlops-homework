from fastapi import FastAPI

from api.models.sentiment import PredictRequest, PredictResponse

app = FastAPI(title="Sentiment Analysis API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    _ = request
    return PredictResponse(prediction="positive")
