from inference import SentimentModelService


def test_sentiment_model_service_returns_positive_stub() -> None:
    service = SentimentModelService()

    prediction = service.predict("I enjoyed the class")

    assert prediction == "positive"
