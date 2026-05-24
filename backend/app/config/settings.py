from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):

    PROJECT_NAME: str
    API_V1: str

    DATABASE_URL: str | None = None
    OPENAI_API_KEY: str

    model_config = {
        "env_file": BASE_DIR / ".env",
        "extra": "ignore"
    }


settings = Settings()