from __future__ import annotations

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
        self.models_root = base_dir / "models"
        self.encoder_dir = self.models_root / "sentence_transformer.model"
        self.classifier_path = self.models_root / "classifier.joblib"

        self._validate_model_files()

        self.encoder = SentenceTransformer(str(self.encoder_dir))
        self.classifier = joblib.load(self.classifier_path)

    def _validate_model_files(self) -> None:
        if not self.encoder_dir.exists():
            msg = f"Sentence Transformer directory not found: {self.encoder_dir}"
            raise FileNotFoundError(msg)

        if not self.classifier_path.exists():
            msg = f"Classifier file not found: {self.classifier_path}"
            raise FileNotFoundError(msg)

    def predict(self, text: str) -> str:
        embedding = self.encoder.encode([text])
        prediction = self.classifier.predict(embedding)[0]
        return CLASS_MAPPING[int(prediction)]
