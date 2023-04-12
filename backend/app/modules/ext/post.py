from math import ceil
from datetime import datetime

from fastapi import HTTPException
from fastapi.concurrency import run_in_threadpool

from sqlalchemy.ext.asyncio import AsyncSession

from core.jwt import get_user_by_token

from modules.database.orm.post import get_post
from modules.database.orm.post import delete_post
from modules.database.orm.post import update_post
from modules.database.orm.post import create_post
from modules.database.orm.post import get_count_post
from modules.database.orm.post import get_multiply_post
from modules.database.orm.post import get_multiply_posts_user

from core.settings import settings


def _caculate_reading_time(text: str, char_per_second: int = 1200) -> int:
    """ Calculating the estimated reading time of a post based
    on the number of characters and the average reading speed.
    """
    characters = len(text)
    minutes = ceil(characters/char_per_second)
    return minutes


async def create_user_post(token: str, session: AsyncSession, text: str, title: str):
    """Creating a new post by id if the user does not have the appropriate rights.
    """
    user_id, role_id = await run_in_threadpool(get_user_by_token, token)
    if not role_id == settings.ADMIN_ROLE_ID:
        raise HTTPException(403, "Access denied")

    reading_time = _caculate_reading_time(text)
    result = await create_post(
        session,
        author=user_id,
        text=text,
        title=title,
        reading_time=reading_time
    )
    return result


async def get_user_post(post_id: int, session: AsyncSession):
    """Getting post data if it exists or is not under moderation.
    """
    post = await get_post(post_id, session)
    if not post:
        raise HTTPException(404, "Post not found!")
    return post


async def delete_user_post(post_id: int, token: str, session: AsyncSession):
    """Deleting a post by id if the user does not have the appropriate rights.
    """
    _, role_id = await run_in_threadpool(get_user_by_token, token)
    if not role_id == settings.ADMIN_ROLE_ID:
        raise HTTPException(403, "Access denied")

    post = await delete_post(post_id, session)
    return post


async def update_user_post(post_id: int, token: str, session: AsyncSession, text: str, title: str):
    """Updating post data by id if the user does not have the appropriate rights.
    """
    _, role_id = await run_in_threadpool(get_user_by_token, token)
    if not role_id == settings.ADMIN_ROLE_ID:
        raise HTTPException(403, "Access denied")

    now_utc = datetime.utcnow()
    post = await update_post(post_id, session, text=text, title=title, update_at=now_utc)
    return post


async def get_multiply_user_posts(page: int, limit: int, session: AsyncSession):
    """Getting a list of posts. available for viewing.
    """
    posts_id = page * limit - limit
    posts = await get_multiply_post(posts_id, limit, session)

    if len(posts) == 0:
        raise HTTPException(404, "Posts not found")

    # Counting the total number of pages
    total_posts = await get_count_post(session)
    total_pages: int = ceil(total_posts[0] / limit)
    return posts, total_pages


async def get_all_user_posts(user_id: int, page: int, limit: int, session: AsyncSession):
    posts_id = page * limit - limit
    posts = await get_multiply_posts_user(user_id, posts_id, limit, session)

    if len(posts) == 0:
        raise HTTPException(404, "Posts not found")

    total_posts = await get_count_post(session)
    total_pages: int = ceil(total_posts[0] / limit)
    return posts, total_pages
