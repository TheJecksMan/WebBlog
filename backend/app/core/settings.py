from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG_MODE: bool

    class Config:
        env_file = "../.env"
        case_sensitive = True


settings = Settings()
