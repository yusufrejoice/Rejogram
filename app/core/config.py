from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class Config(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REJOGRAM_DATABASE_URL : str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Create settings object
settings = Config()