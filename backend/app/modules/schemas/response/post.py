import orjson

from typing import List
from datetime import datetime

from pydantic import BaseModel


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
    post_id: int
    author: int
    title: int
    create_at: datetime


class ResponseMultiplyPost(BaseModel):
    posts: List[ResponseListPost]

    class Config:
        orm_mode = True
        json_loads = orjson.loads
