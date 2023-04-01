from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from modules.database.models import Posts
<<<<<<< HEAD
from modules.database.models import Users


async def create_post(session: AsyncSession, **kwargs):
=======


async def create_post(user_id: int, session: AsyncSession, **kwargs):
>>>>>>> 8a87530f0f2db04279821aaf7999fd187f72fdbf
    result = await session.execute(insert(Posts).values(**kwargs))
    return result


async def update_post(post_id: int, session: AsyncSession, **kwargs):
    result = await session.execute(update(Posts).where(Posts.id == post_id).values(**kwargs))
    return result


async def get_post_by_id(post_id: int, session: AsyncSession):
    result = await session.execute(select(Posts).where(Posts.id == post_id))
    return result.first()


<<<<<<< HEAD
async def get_multiply_post(posts_id: int, limit: int, session: AsyncSession):
    result = await session.execute(
        select(Posts.id, Posts.create_at, Posts.title, Users.username)
        .join(Users)
        .where(Posts.id >= posts_id)
        .order_by(Posts.create_at.asc())
        .limit(limit)
    )
    return result.all()


=======
>>>>>>> 8a87530f0f2db04279821aaf7999fd187f72fdbf
async def delete_post_by_id(post_id: int, session: AsyncSession):
    result = await session.execute(delete(Posts).where(Posts.id == post_id))
    return result
