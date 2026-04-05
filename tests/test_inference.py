import pytest

from inference import SentimentInferenceService


@pytest.fixture(scope="module")
def service() -> SentimentInferenceService:
    return SentimentInferenceService()


def test_model_loads_without_errors(service: SentimentInferenceService) -> None:
    assert service is not None
    assert service.encoder is not None
    assert service.classifier is not None


@pytest.mark.parametrize(
    "text",
    [
        "I absolutely loved this lecture.",
        "It was okay, nothing special.",
        "This was a terrible experience.",
    ],
)
def test_inference_works_for_sample_strings(
    service: SentimentInferenceService, text: str
) -> None:
    prediction = service.predict(text)

    assert isinstance(prediction, str)
    assert prediction in {"negative", "neutral", "positive"}
