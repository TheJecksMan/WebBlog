from datetime import datetime
from pydantic import BaseModel

from core.orjson import orjson_dumps


class Token(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        json_dumps = orjson_dumps


class AccessToken(BaseModel):
    access_token: str

    class Config:
        json_dumps = orjson_dumps


class CurrentUser(BaseModel):
    id: int
    username: str
    status: str
    avatar_url: str | None
    create_at: datetime
    is_active: bool
    name: str
    color: str

    class Config:
        orm_mode = True
        json_dumps = orjson_dumps
