from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from modules.database.models import Users


async def get_user_by_username(username: str, session: AsyncSession):
    result = await session.execute(
        select(Users.id, Users.username, Users.password, Users.is_active)
        .where(Users.username == username)
    )
    return result.first()


async def insert_user(session: AsyncSession, **kwargs):
    await session.execute(insert(Users).values(**kwargs))
