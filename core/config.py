from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from enum import Enum


class Environment(str, Enum):
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    ENVIRONMENT: Environment = Environment.LOCAL

    DATABASE_URL: PostgresDsn


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
