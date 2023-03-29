from starlette.concurrency import run_in_threadpool

from sqlalchemy.ext.asyncio import AsyncSession

from core.jwt import get_user_id_token

from modules.database.orm.post import create_post


async def create_user_post(access_token: str, session: AsyncSession, **kwargs):
    user_id = await run_in_threadpool(get_user_id_token, access_token)
    result = await create_post(session)
