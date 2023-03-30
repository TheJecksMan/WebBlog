from starlette.concurrency import run_in_threadpool

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from core.jwt import get_user_id_token

from modules.database.models import Posts
from modules.database.orm.post import create_post
from modules.database.orm.post import get_post_by_id


async def create_user_post(access_token: str, session: AsyncSession, **kwargs):
    user_id = await run_in_threadpool(get_user_id_token, access_token)
    result = await create_post(session)


async def get_user_post(post_id: int, session: AsyncSession):
    """Getting post data if it exists or is not under moderation.
    """
    post: Posts = await get_post_by_id(post_id, session)

    if not post:
        raise HTTPException(404, "Post not found!")
    elif not post.is_moderated:
        raise HTTPException(400, "Post in moderation")
    return post
