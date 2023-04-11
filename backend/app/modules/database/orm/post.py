from sqlalchemy import func
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from modules.database.models import Posts
from modules.database.models import Users


async def create_post(session: AsyncSession, **kwargs):
    result = await session.execute(
        insert(Posts)
        .values(**kwargs).returning(Posts.id)
    )
    return result.first()


async def update_post(post_id: int, session: AsyncSession, **kwargs):
    result = await session.execute(
        update(Posts)
        .where(Posts.id == post_id)
        .values(**kwargs).returning(Posts.id))
    return result.first()


async def get_post_by_id(post_id: int, session: AsyncSession):
    result = await session.execute(
        select(Posts.id, Posts.title, Posts.text, Posts.create_at,
               Users.username, Posts.reading_time)
        .join(Users)
        .where(Posts.id == post_id))
    return result.first()


async def get_multiply_post(posts_id: int, limit: int, session: AsyncSession):
    result = await session.execute(
        select(Posts.id, Posts.create_at, Posts.title, Users.username, Posts.reading_time)
        .join(Users)
        .where(Posts.id > posts_id)
        .order_by(Posts.create_at.desc())
        .limit(limit)
    )
    return result.all()


async def delete_post_by_id(post_id: int, session: AsyncSession):
    result = await session.execute(
        delete(Posts)
        .where(Posts.id == post_id)
        .return_defaults(Posts.id)
    )
    return result.first()


async def get_count_post(session: AsyncSession):
    result = await session.execute(select(func.count(Posts.id)))
    return result.first()
