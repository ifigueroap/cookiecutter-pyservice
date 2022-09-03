"""Settings for the {{cookiecutter.project_name}} project."""


from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Global settings for the {{cookiecutter.project_name}} project."""

    SAMPLE_FIELD: str = Field(None, env="SAMPLE_FIELD")

    class Config:
        """Sets up settings to read config values from .env file."""

        env_file = ".env"


settings = Settings()
