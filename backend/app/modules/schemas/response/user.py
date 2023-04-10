from datetime import datetime
from pydantic import BaseModel

from core.orjson import orjson_dumps


class ResponseToken(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        json_dumps = orjson_dumps


class ResponseAccessToken(BaseModel):
    access_token: str

    class Config:
        json_dumps = orjson_dumps


class ResponseCurrentUser(BaseModel):
    id: int
    username: str
    avatar_url: str | None
    create_at: datetime
    is_active: bool
    name: str
    color: str

    class Config:
        orm_mode = True
        json_dumps = orjson_dumps
