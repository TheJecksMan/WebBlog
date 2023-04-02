from pydantic import Field
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Application
    TITLE_APP: str = "Back-end for Blog"
    VERSION_APP: str = "0.2.0"

    # Database
    DATABASE_URL: str
    DEBUG_MODE: bool = Field(default=False)

    # JWT
    ACCESS_TOKEN_EXPIRED: int
    REFRESH_TOKEN_EXPIRED: int

    SECRET_ACCESS_TOKEN: str
    SECRET_REFRESH_TOKEN: str

    # JWT ROLES
    USER_ROLE_ID = 3
    MODERATED_ROLE_ID = 2
    ADMIN_ROLE_ID = 1

    class Config:
        env_file = "../.env"
        case_sensitive = True


settings = Settings()
