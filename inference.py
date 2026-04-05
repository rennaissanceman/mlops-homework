from pathlib import Path

import joblib
from sentence_transformers import SentenceTransformer

CLASS_MAPPING = {
    0: "negative",
    1: "neutral",
    2: "positive",
}


class SentimentInferenceService:
    def __init__(self) -> None:
        base_dir = Path(__file__).resolve().parent
        model_dir = base_dir / "models" / "sentiment"

        self.encoder = SentenceTransformer(
            str(model_dir / "sentence_transformer.model")
        )
        self.classifier = joblib.load(model_dir / "classifier.joblib")

    def predict(self, text: str) -> str:
        embedding = self.encoder.encode([text], convert_to_numpy=True)
        predicted_class = self.classifier.predict(embedding)[0]
        return CLASS_MAPPING[int(predicted_class)]
