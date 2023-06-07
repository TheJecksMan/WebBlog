from datetime import datetime
from pydantic import BaseModel
from pydantic import Field

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


class IDUser(BaseModel):
    id: int = Field(alias='user_id')
    
    class Config:
        orm_mode = True
        json_dumps = orjson_dumps
        allow_population_by_field_name = True
