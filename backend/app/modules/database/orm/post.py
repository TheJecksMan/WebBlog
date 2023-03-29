from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from modules.database.models import Posts


async def create_post(session: AsyncSession, **kwargs):
    result = await session.execute(insert(Posts).values(**kwargs))
    return result


async def update_post(post_id: int, session: AsyncSession, **kwargs):
    result = await session.execute(update(Posts).where(Posts.id == post_id).values(**kwargs))
    return result


async def get_post_by_id(post_id: int, session: AsyncSession):
    result = await session.execute(select(Posts).where(Posts.id == post_id))
    return result.first()


async def delete_post_by_id(post_id: int, session: AsyncSession):
    result = await session.execute(delete(Posts).where(Posts.id == post_id))
    return result
