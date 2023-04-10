from typing import List
from datetime import datetime

from pydantic import Field
from pydantic import BaseModel

from core.orjson import orjson_dumps


class ResponsePost(BaseModel):
    id: str
    username: str = Field(alias='author')
    title: str
    text: str
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
