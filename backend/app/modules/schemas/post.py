from pydantic import BaseModel


class CreateUserPost(BaseModel):
    title: str
    text: str


class Post(BaseModel):
    post_id: int


class UpdateUserPost(Post):
    title: str
    text: str
