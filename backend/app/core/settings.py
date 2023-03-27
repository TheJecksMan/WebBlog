from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG_MODE: bool

    ACCESS_TOKEN_EXPIRED: int
    REFRESH_TOKEN_EXPIRED: int

    SECRET_ACCESS_TOKEN: str
    SECRET_REFRESH_TOKEN: str

    class Config:
        env_file = "../.env"
        case_sensitive = True


settings = Settings()
