import os
from pydantic import BaseSettings

# ASYNC_DATABASE_URL = os.environ['DATABASE_URL']

# DEBUG_MODE = os.getenv('DEBUG_MODE', False)


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG_MODE: bool

    class Config:
        env_file = "../.env"
        case_sensitive = True


settings = Settings()
