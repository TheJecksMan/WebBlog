from datetime import datetime
from pydantic import BaseModel
from pydantic import Field


class Token(BaseModel):
    access_token: str
    refresh_token: str


class AccessToken(BaseModel):
    access_token: str


class CurrentUser(BaseModel):
    id: int
    username: str
    status: str
    avatar_url: str | None
    create_at: datetime
    is_active: bool
    name: str
    color: str

    class Config:
        from_attributes = True


class IDUser(BaseModel):
    id: int = Field(alias='user_id')

    class Config:
        from_attributes = True
        populate_by_name = True
