import orjson

from datetime import datetime
from pydantic import BaseModel


class ResponseToken(BaseModel):
    access_token: str
    refresh_token: str


class ResponseRefreshToken(BaseModel):
    refresh_token: str


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
        json_loads = orjson.loads
