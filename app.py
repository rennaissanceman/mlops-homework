from fastapi import FastAPI

from api.models.sentiment import PredictRequest, PredictResponse
from inference import SentimentInferenceService

app = FastAPI()

sentiment_service = SentimentInferenceService()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    prediction = sentiment_service.predict(request.text)
    return PredictResponse(prediction=prediction)
