import orjson

from pydantic import Field
from pydantic import BaseModel


class ChangePassword(BaseModel):
    password: str = Field(min_length=4, max_length=40, regex=r"^[A-Za-z0-9!@_]*$")

    class Config:
        json_loads = orjson.loads


class UpdateStatus(BaseModel):
    status: str = Field(max_length=60)

    class Config:
        json_loads = orjson.loads
