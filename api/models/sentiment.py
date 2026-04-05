from pydantic import BaseModel, field_validator


class PredictRequest(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("text must be a non-empty string")
        return value


class PredictResponse(BaseModel):
    prediction: str
