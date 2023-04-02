from typing import Tuple
from fastapi import HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from starlette.concurrency import run_in_threadpool

from core.settings import settings
from core.jwt import generate_token
from core.jwt import update_access_token
from core.jwt import get_user_by_token
from core.security import verify_password
from core.security import get_password_hash

from modules.database.models import Users
from modules.database.orm.user import insert_user
from modules.database.orm.user import get_current_user
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

    access, refresh = await run_in_threadpool(generate_token, user.id, user.role_id)
    return access, refresh


async def create_user(username: str, email: str, password: str, session: AsyncSession):
    """ User registration in the database.
    The password obtained from the parameters is securely hashed by the bcrypt algorithm.
    """
    hashed_password = await run_in_threadpool(get_password_hash, password)
    try:
        await insert_user(
            session,
            username=username,
            email=email,
            password=hashed_password,
            role_id=settings.USER_ROLE_ID
        )
    except IntegrityError:
        raise HTTPException(400, "Username and/or email is already in use")


async def current_user(token: str, session: AsyncSession):
    """ Getting data about the current user by access token, if possible.
    """
    user_id, _ = await run_in_threadpool(get_user_by_token, token)
    if not user_id:
        raise HTTPException(403, "Uncorrect token")

    user = await get_current_user(user_id, session)
    if not user:
        raise HTTPException(400, "Unccorrect user")
    return user


async def update_token(token: str) -> str:
    """ Updating the access token if it has expired. Getting a new one.
    """
    access = await run_in_threadpool(update_access_token, token)
    if not access:
        raise HTTPException(400, "Uncorrect refresh token")
    return access
