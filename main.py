import argparse
import os

import yaml
from dotenv import load_dotenv

from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file_mapping = {
        "dev": "config/.env.dev",
        "test": "config/.env.test",
        "prod": "config/.env.prod",
    }

    if environment not in env_file_mapping:
        raise ValueError(
            f"Invalid environment argument: {environment}. Allowed: dev, test, prod"
        )

    env_file_path = env_file_mapping[environment]

    if not os.path.exists(env_file_path):
        raise FileNotFoundError(f"Environment file not found: {env_file_path}")

    load_dotenv(env_file_path, override=True)


def load_secrets_to_env(secrets_file_path: str = "secrets.yaml") -> None:
    if not os.path.exists(secrets_file_path):
        raise FileNotFoundError(f"Secrets file not found: {secrets_file_path}")

    with open(secrets_file_path, "r", encoding="utf-8") as file:
        secrets = yaml.safe_load(file)

    if not isinstance(secrets, dict):
        raise ValueError("Secrets file must contain a YAML dictionary.")

    for key, value in secrets.items():
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables and secrets."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_secrets_to_env("secrets.yaml")

    settings = Settings()

    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("API_KEY:", settings.API_KEY)
    print("DB_PASSWORD:", settings.DB_PASSWORD)
