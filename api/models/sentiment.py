from pydantic import BaseModel, field_validator


class PredictRequest(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Text must not be empty")
        return value


class PredictResponse(BaseModel):
    prediction: str
