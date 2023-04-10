import orjson

from pydantic import Field
from pydantic import BaseModel


class CreateUserPost(BaseModel):
    title: str = Field(max_length=30_000)
    text: str = Field(max_length=30_000)

    class Config:
        json_loads = orjson.loads


class UpdateUserPost(BaseModel):
    post_id: int = Field(ge=1, le=100_000)
    title: str = Field(max_length=300)
    text: str = Field(max_length=30_000)

    class Config:
        json_loads = orjson.loads
