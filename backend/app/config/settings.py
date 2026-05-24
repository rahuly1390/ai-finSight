from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(
    BaseSettings
):

    PROJECT_NAME: str = (
        "FinSight AI"
    )

    API_V1: str = (
        "/api/v1"
    )

    DATABASE_URL: str = (
        "sqlite:///./finsight.db"
    )

    OPENAI_API_KEY: str = (
        "dummy-key"
    )

    model_config = (
        SettingsConfigDict(
            env_file=".env",
            extra="ignore"
        )
    )


settings = Settings()