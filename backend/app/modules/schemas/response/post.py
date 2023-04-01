import orjson

from typing import List
from datetime import datetime

from pydantic import BaseModel
<<<<<<< HEAD
from pydantic import Field
=======
>>>>>>> 8a87530f0f2db04279821aaf7999fd187f72fdbf


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
<<<<<<< HEAD
    id: int
    username: str = Field(alias='author')
    title: str
    create_at: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

=======
    post_id: int
    author: int
    title: int
    create_at: datetime

>>>>>>> 8a87530f0f2db04279821aaf7999fd187f72fdbf

class ResponseMultiplyPost(BaseModel):
    posts: List[ResponseListPost]

    class Config:
        orm_mode = True
        json_loads = orjson.loads
