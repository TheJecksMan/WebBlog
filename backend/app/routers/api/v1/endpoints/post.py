from typing import Annotated

from fastapi import Depends
from fastapi import APIRouter

from sqlalchemy.ext.asyncio import AsyncSession

from routers.api.deps import oauth2_scheme
from routers.api.deps import get_async_session

from modules.ext.post import get_user_post

from modules.schemas.post import CreateUserPost as CUPost
from modules.schemas.post import UpdateUserPost as UUPost
from modules.schemas.response.post import ResponsePost as RPost


router = APIRouter()


@router.post("/create")
async def create_user_post(
    post: CUPost,
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    pass


@router.put("/update")
async def update_user_post(
    post: UUPost,
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    pass


@router.delete("/delete")
async def delete_user_post(
    id: int,
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    pass


@router.get("", response_model=RPost)
async def get_post(
    id: int,
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    post = await get_user_post(id, session)
    return post


@router.get("/multiply")
async def get_multiply_posts(
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    pass
