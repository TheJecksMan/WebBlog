from typing import Tuple
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from starlette.concurrency import run_in_threadpool

from core.jwt import generate_token
from core.security import verify_password
from core.security import get_password_hash

from modules.database.models import Users
from modules.database.orm.user import insert_user
from modules.database.orm.user import get_user_by_username


async def authenticate_user(username: str, password: str, session: AsyncSession) -> Tuple[str, str]:
    """Database user authentication. Getting a JWT Token
    """
    user: Users = await get_user_by_username(username, session)
    # User not registered
    if not user:
        raise HTTPException(400, "Incorrect user and/or password")

    # Banned user
    if not user.is_active:
        raise HTTPException(403, "Innactive user")

    hashed_password = await run_in_threadpool(verify_password, password, user.password)
    # Invalid password hash
    if not hashed_password:
        raise HTTPException(400, "Incorrect user and/or password")

    access, refresh = await run_in_threadpool(generate_token, user.id)
    return access, refresh


async def create_user(username: str, email: str, password: str, session: AsyncSession):
    """User registration in the database.
    The password obtained from the parameters is securely hashed by the bcrypt algorithm.
    """
    hashed_password = await run_in_threadpool(get_password_hash, password)
    try:
        await insert_user(session, username=username, email=email, password=hashed_password)
    except IntegrityError:
        raise HTTPException(400, "Username and/or email is already in use")
