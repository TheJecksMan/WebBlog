from typing import List
from datetime import datetime

from pydantic import Field
from pydantic import BaseModel

from core.orjson import orjson_dumps


class ResponseBasePost(BaseModel):
    id: int = Field(alias='post_id')

    class Config:
        orm_mode = True
        json_dumps = orjson_dumps
        allow_population_by_field_name = True


class ResponsePost(BaseModel):
    id: str
    username: str = Field(alias='author')
    title: str
    text: str
    reading_time: int
    create_at: datetime
    update_at: datetime | None

    class Config:
        orm_mode = True
        json_dumps = orjson_dumps
        allow_population_by_field_name = True


class ResponseListPost(BaseModel):
    id: int
    username: str = Field(alias='author')
    title: str
    reading_time: int
    create_at: datetime

    class Config:
        orm_mode = True
        json_dumps = orjson_dumps
        allow_population_by_field_name = True


class ResponseMultiplyPost(BaseModel):
    posts: List[ResponseListPost]
    total_pages: int

    class Config:
        orm_mode = True
        json_dumps = orjson_dumps
