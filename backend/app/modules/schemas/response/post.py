from typing import List
from datetime import datetime

from pydantic import Field
from pydantic import BaseModel

from core.orjson import orjson_dumps


class BasePost(BaseModel):
    id: int = Field(alias='post_id')

    class Config:
        from_attributes = True
        populate_by_name = True


class Post(BaseModel):
    id: str
    username: str = Field(alias='author')
    title: str
    text: str
    reading_time: int
    create_at: datetime
    update_at: datetime | None

    class Config:
        from_attributes = True
        populate_by_name = True


class ListPost(BaseModel):
    id: int
    username: str = Field(alias='author')
    title: str
    reading_time: int
    create_at: datetime

    class Config:
        from_attributes = True
        populate_by_name = True


class MultiplyPost(BaseModel):
    posts: List[ListPost]
    total_pages: int

    class Config:
        from_attributes = True


class ListAllUserPost(BaseModel):
    id: int
    title: str
    create_at: datetime

    class Config:
        from_attributes = True


class MultiplyAllUserPost(BaseModel):
    posts: List[ListAllUserPost]
    total_pages: int

    class Config:
        from_attributes = True
