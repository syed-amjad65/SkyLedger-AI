# app/core/config.py
"""
Centralized configuration for SkyLedger-AI.
Loads environment variables using Pydantic BaseSettings.
"""

from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    APP_ENV: str = "development"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "sqlite:///./skyledger.db"

    # Security (JWT etc.)
    JWT_SECRET: str = "change_this_secret_in_production"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
