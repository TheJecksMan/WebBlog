import orjson

from typing import List
from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class ResponsePost(BaseModel):
    id: str
    author: int
    title: str
    text: str
    create_at: datetime
    update_at: datetime | None

    class Config:
        orm_mode = True
        json_loads = orjson.loads


class ResponseListPost(BaseModel):
    id: int
    username: str = Field(alias='author')
    title: str
    create_at: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ResponseMultiplyPost(BaseModel):
    posts: List[ResponseListPost]

    class Config:
        orm_mode = True
        json_loads = orjson.loads
