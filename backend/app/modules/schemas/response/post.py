from datetime import datetime

from pydantic import BaseModel


class ResponsePost(BaseModel):
    post_id: str
    author: int
    title: str
    text: str
    create_at: datetime
    update_at: datetime

    class Config:
        orm = True
