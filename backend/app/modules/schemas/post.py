from pydantic import BaseModel

<<<<<<< HEAD
from pydantic import Field

=======
>>>>>>> 8a87530f0f2db04279821aaf7999fd187f72fdbf

class CreateUserPost(BaseModel):
    title: str
    text: str


class Post(BaseModel):
    post_id: int


<<<<<<< HEAD
=======
class PostMultiply(BaseModel):
    page: int


>>>>>>> 8a87530f0f2db04279821aaf7999fd187f72fdbf
class UpdateUserPost(Post):
    post_id: int
    title: str
    text: str
