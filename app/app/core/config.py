import os
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///database.db")
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "congerence_api")

    class Config:
        case_sensitive = True


settings = Settings()
