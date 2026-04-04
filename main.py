import argparse
import os

from dotenv import load_dotenv

from settings import Settings


def export_envs(environment: str = "dev") -> None:
    allowed_environments = {"dev", "test", "prod"}

    if environment not in allowed_environments:
        raise ValueError(
            f"Unsupported environment argument: '{environment}'. "
            f"Allowed values: dev, test, prod."
        )

    env_file_path = os.path.join("config", f".env.{environment}")

    if not os.path.exists(env_file_path):
        raise FileNotFoundError(f"Environment file not found: {env_file_path}")

    load_dotenv(dotenv_path=env_file_path, override=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
