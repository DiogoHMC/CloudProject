from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    # LLM provider selection: "openai", "gemini", "mock", "local"
    LLM_PROVIDER: str = "mock"
    OPENAI_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    # Gemini model to use (include 'models/' prefix if required by API)
    GEMINI_MODEL: str = "models/gemini-2.5-flash"

    class Config:
        env_file = ".env"

settings = Settings()
