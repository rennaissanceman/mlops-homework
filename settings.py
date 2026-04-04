from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str) -> str:
        allowed_environments = {"dev", "test", "prod"}

        if value not in allowed_environments:
            raise ValueError(
                f"Invalid ENVIRONMENT='{value}'. Allowed values: dev, test, prod."
            )

        return value
