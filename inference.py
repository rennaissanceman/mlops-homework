from __future__ import annotations

import zipfile
from pathlib import Path

import joblib  # type: ignore[import-untyped]
from sentence_transformers import SentenceTransformer

CLASS_MAPPING = {
    0: "negative",
    1: "neutral",
    2: "positive",
}

MODEL_ARCHIVE_URL = (
    "https://drive.google.com/file/d/1NRZdYq5jweVRUzAZG518LMhs4E56IgxG/view"
)


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

        try:
            import gdown  # type: ignore[import-untyped]
        except ImportError as exc:
            raise RuntimeError(
                "Missing optional dependency 'gdown'. Install it with: uv add gdown"
            ) from exc

        gdown.download(
            url=MODEL_ARCHIVE_URL,
            output=str(self.archive_path),
            quiet=False,
            fuzzy=True,
        )

        if not self.archive_path.exists():
            raise FileNotFoundError("Model archive was not downloaded successfully.")

        with zipfile.ZipFile(self.archive_path, "r") as zip_ref:
            zip_ref.extractall(self.models_root)

        if self.archive_path.exists():
            self.archive_path.unlink()

        if not self.encoder_dir.exists():
            raise FileNotFoundError(
                f"Missing encoder directory after extraction: {self.encoder_dir}"
            )

        if not self.classifier_path.exists():
            raise FileNotFoundError(
                f"Missing classifier file after extraction: {self.classifier_path}"
            )

    def predict(self, text: str) -> str:
        cleaned_text = text.strip()
        if not cleaned_text:
            raise ValueError("Input text must not be empty.")

        embedding = self.encoder.encode([cleaned_text], convert_to_numpy=True)
        predicted_class = self.classifier.predict(embedding)[0]
        return CLASS_MAPPING[int(predicted_class)]


SentimentModelService = SentimentInferenceService
