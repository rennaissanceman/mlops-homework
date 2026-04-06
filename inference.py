from __future__ import annotations

import zipfile
from pathlib import Path

import gdown
import joblib
from sentence_transformers import SentenceTransformer

CLASS_MAPPING = {
    0: "negative",
    1: "neutral",
    2: "positive",
}

MODEL_ARCHIVE_URL = "https://drive.google.com/uc?id=1NRZdYq5jweVRUzAZG518LMhs4E56IgxG"


class SentimentInferenceService:
    def __init__(self) -> None:
        base_dir = Path(__file__).resolve().parent
        self.models_root = base_dir / "models"
        self.encoder_dir = self.models_root / "sentence_transformer.model"
        self.classifier_path = self.models_root / "classifier.joblib"
        self.archive_path = self.models_root / "sentiment_model.zip"

        self._prepare_model()

        self.encoder = SentenceTransformer(str(self.encoder_dir))
        self.classifier = joblib.load(self.classifier_path)

    def _prepare_model(self) -> None:
        if self.encoder_dir.exists() and self.classifier_path.exists():
            return

        self.models_root.mkdir(parents=True, exist_ok=True)

        if not self.archive_path.exists():
            gdown.download(
                MODEL_ARCHIVE_URL,
                str(self.archive_path),
                quiet=False,
            )

        with zipfile.ZipFile(self.archive_path, "r") as archive:
            archive.extractall(self.models_root)

        self._validate_model_files()

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
