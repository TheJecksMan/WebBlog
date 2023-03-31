from pydantic import BaseModel


class CreateUserPost(BaseModel):
    title: str
    text: str


class Post(BaseModel):
    post_id: int


class PostMultiply(BaseModel):
    page: int


class UpdateUserPost(Post):
    post_id: int
    title: str
    text: str
