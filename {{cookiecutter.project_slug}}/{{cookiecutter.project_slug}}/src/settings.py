"""Settings for the {{cookiecutter.project_name}} project."""


from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Global settings for the Python Service Boilerplate project."""

    version: str = Field("1.0", env="VERSION")
    commit: str = Field("local", env="COMMIT")
    LOG_LEVEL: str = Field("DEBUG", env="LOG_LEVEL")

    CELERY_BROKER_URL: str = Field(None, env="CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = Field(None, env="CELERY_RESULT_BACKEND")

    class Config:
        """Sets up settings to read config values from .env file."""

        env_file = ".env"


settings = Settings()
