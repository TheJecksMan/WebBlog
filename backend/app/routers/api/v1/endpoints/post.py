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
from modules.ext.post import get_all_user_posts
from modules.ext.post import get_multiply_user_posts

from modules.schemas.post import CreateUserPost as CUPost
from modules.schemas.post import UpdateUserPost as UUPost

from modules.schemas.response.base import DetailResponse

from modules.schemas.response.post import Post
from modules.schemas.response.post import BasePost as BPost
from modules.schemas.response.post import MultiplyPost as MPost
from modules.schemas.response.post import MultiplyAllUserPost as MAUPost


router = APIRouter()

JWTToken = Annotated[str, Depends(oauth2_scheme)]
Session = Annotated[AsyncSession, Depends(get_async_session)]
PostID = Annotated[int, Query(ge=1, le=100_000)]


@router.post(
    "/create",
    response_model=BPost,
    responses={
        403: {"model": DetailResponse}
    })
async def create_post(post: CUPost, token: JWTToken, session: Session):
    post_data = await create_user_post(token, session, post.text, post.title)
    return post_data


@router.put(
    "/update",
    response_model=BPost,
    responses={
        403: {"model": DetailResponse}
    })
async def update_post(post: UUPost, token: JWTToken, session: Session):
    post_data = await update_user_post(post.post_id, token, session, post.text, post.title)
    return post_data


@router.delete(
    "/delete",
    response_model=BPost,
    responses={
        403: {"model": DetailResponse}
    })
async def delete_post(id: PostID, token: JWTToken, session: Session):
    post_data = await delete_user_post(id, token, session)
    return post_data


@router.get(
    "",
    response_model=Post,
    responses={
        404: {"model": DetailResponse}
    })
async def get_post(id: PostID, session: Session):
    post = await get_user_post(id, session)
    return post


@router.get(
    "/multiply",
    response_model=MPost,
    responses={
        404: {"model": DetailResponse}
    })
async def get_multiply_posts(
    page: Annotated[int, Query(ge=1, le=350)],
    limit: Annotated[int, Query(ge=5, le=20)],
    session: Session
):
    posts, t_pages = await get_multiply_user_posts(page, limit, session)
    return MPost(posts=posts, total_pages=t_pages)


@router.get(
    "/user/all",
    response_model=MAUPost,
    responses={
        404: {"model": DetailResponse}
    })
async def get_user_posts(
    user_id: Annotated[int, Query(ge=1, le=2**63-1)],
    page: Annotated[int, Query(ge=1, le=350)],
    limit: Annotated[int, Query(ge=5, le=20)],
    session: Session
):
    posts, t_pages = await get_all_user_posts(user_id, page, limit, session)
    return MAUPost(posts=posts, total_pages=t_pages)
