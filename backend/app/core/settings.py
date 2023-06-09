from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    TITLE_APP: str = "Back-end for Blog"
    VERSION_APP: str = "0.2.1"

    # Sentry
    ENABLE_SENTRY: bool = Field(True)
    SENTRY_DSN: str

    # Database
    DATABASE_URL: str
    DEBUG_MODE: bool = Field(default=False)

    # JWT
    ACCESS_TOKEN_EXPIRED: int = Field(default=15)  # minutes
    REFRESH_TOKEN_EXPIRED: int = Field(default=3)  # days

    SECRET_ACCESS_TOKEN: str
    SECRET_REFRESH_TOKEN: str

    # JWT ROLES
    USER_ROLE_ID: int = 3
    MODERATED_ROLE_ID: int = 2
    ADMIN_ROLE_ID: int = 1

    class Config:
        env_file = "../.env"
        case_sensitive = True


settings = Settings()
