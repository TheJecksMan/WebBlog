from pydantic import Field
from pydantic import BaseModel


class ChangePassword(BaseModel):
    password: str = Field(min_length=4, max_length=40, pattern=r"^[A-Za-z0-9!@_]*$")


class UpdateStatus(BaseModel):
    status: str = Field(max_length=60)
