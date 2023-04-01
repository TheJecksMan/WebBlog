from typing import Annotated

from fastapi import Query
from fastapi import Depends
from fastapi import APIRouter

from sqlalchemy.ext.asyncio import AsyncSession

from routers.api.deps import oauth2_scheme
from routers.api.deps import get_async_session

from modules.ext.post import get_user_post
from modules.ext.post import create_user_post
from modules.ext.post import delete_user_post
from modules.ext.post import update_user_post
from modules.ext.post import get_multiply_user_posts

from modules.schemas.post import CreateUserPost as CUPost
from modules.schemas.post import UpdateUserPost as UUPost
from modules.schemas.response.post import ResponsePost as RPost
from modules.schemas.response.post import ResponseMultiplyPost as RMPost


router = APIRouter()

JWTToken = Annotated[str, Depends(oauth2_scheme)]
Session = Annotated[AsyncSession, Depends(get_async_session)]


@router.post("/create")
async def create_post(post: CUPost, token: JWTToken, session: Session):
    post_data = await create_user_post(token, session, post.text, post.title)
    return post_data


@router.put("/update")
async def update_post(post: UUPost, token: JWTToken, session: Session):
    post_data = await update_user_post(post.post_id, token, session, post.text, post.title)
    return post_data


@router.delete("/delete")
async def delete_post(id: int, token: JWTToken, session: Session):
    post_data = await delete_user_post(id, token, session)
    return post_data


@router.get("", response_model=RPost)
async def get_post(id: int, session: Session):
    post = await get_user_post(id, session)
    return post


@router.get("/multiply", response_model=RMPost)
async def get_multiply_posts(
    page: Annotated[int, Query(ge=1)],
    limit: Annotated[int, Query(ge=5, le=10)],
    session: Session
):
    posts = await get_multiply_user_posts(page, limit, session)
    print(posts[0]._mapping)
    return RMPost(posts=posts)
