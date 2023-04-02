from pydantic import Field
from pydantic import BaseModel


class ChangePassword(BaseModel):
    password: str = Field(min_length=4, max_length=32, regex=r"^[A-Za-z0-9!@_]*$")
