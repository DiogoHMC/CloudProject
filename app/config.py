# app/config.py
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    ENV: str = "development"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    # LLM provider selection: "openai", "gemini", "mock", "local"
    LLM_PROVIDER: str = "mock"
    OPENAI_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    # Gemini model (sem prefixo "models/")
    GEMINI_MODEL: str = "gemini-2.5-flash"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
