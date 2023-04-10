import orjson

from pydantic import Field
from pydantic import BaseModel
from pydantic import EmailStr


class RegistrationUser(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=32, regex=r"^[A-Za-z0-9_]*$")
    password: str = Field(min_length=4, max_length=32, regex=r"^[A-Za-z0-9!@_]*$")

    class Config:
        json_loads = orjson.loads


class RefreshToken(BaseModel):
    refresh_token: str

    class Config:
        json_loads = orjson.loads
