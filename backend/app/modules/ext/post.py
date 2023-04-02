from datetime import datetime

from starlette.concurrency import run_in_threadpool

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from core.jwt import get_user_by_token

from modules.database.models import Posts
from modules.database.orm.post import update_post
from modules.database.orm.post import create_post
from modules.database.orm.post import get_post_by_id
from modules.database.orm.post import delete_post_by_id
from modules.database.orm.post import get_multiply_post

from core.settings import settings


async def create_user_post(token: str, session: AsyncSession, text: str, title: str):
    """Creating a new post by id if the user does not have the appropriate rights.
    """
    user_id, role_id = await run_in_threadpool(get_user_by_token, token)
    if not role_id == settings.ADMIN_ROLE_ID:
        raise HTTPException(403, "Access denied")

    result = await create_post(session, author=user_id, text=text, title=title)
    return result


async def get_user_post(post_id: int, session: AsyncSession):
    """Getting post data if it exists or is not under moderation.
    """
    post: Posts = await get_post_by_id(post_id, session)
    if not post:
        raise HTTPException(404, "Post not found!")
    return post[0]


async def delete_user_post(post_id: int, token: str, session: AsyncSession):
    """Deleting a post by id if the user does not have the appropriate rights.
    """
    _, role_id = await run_in_threadpool(get_user_by_token, token)
    if not role_id == settings.ADMIN_ROLE_ID:
        raise HTTPException(403, "Access denied")

    post = delete_post_by_id(post_id, session)
    return post


async def update_user_post(post_id: int, token: str, session: AsyncSession, text: str, title: str):
    """Updating post data by id if the user does not have the appropriate rights.
    """
    _, role_id = await run_in_threadpool(get_user_by_token, token)
    if not role_id == settings.ADMIN_ROLE_ID:
        raise HTTPException(403, "Access denied")

    now_utc = datetime.utcnow()
    post = update_post(post_id, session, text=text, title=title, update_at=now_utc)
    return post


async def get_multiply_user_posts(page: int, limit: int, session: AsyncSession):
    """Getting a list of posts. available for viewing.
    """
    posts_id = page * limit - limit
    posts = await get_multiply_post(posts_id, limit, session)

    if len(posts) == 0:
        raise HTTPException(404, "Posts not found")
    return posts
