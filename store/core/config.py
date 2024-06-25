from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Store API"
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env_settings")


settings = Settings()
