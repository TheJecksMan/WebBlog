from sqlalchemy.ext.asyncio import AsyncSession

from starlette.concurrency import run_in_threadpool

from core.jwt import get_user_by_token
from core.security import get_password_hash

from modules.database.orm.user import update_user


async def change_user_password(password: str, token: str, session: AsyncSession):
    """User password update. Getting its id by JWT
    """
    user_id, _ = await run_in_threadpool(get_user_by_token, token)
    hashed_password = await run_in_threadpool(get_password_hash, password)

    await update_user(user_id, session, password=hashed_password)
