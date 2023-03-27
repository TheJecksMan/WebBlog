from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import Response

from sqlalchemy.ext.asyncio import AsyncSession

from routers.api.deps import get_async_session
from modules.ext.user import authenticate_user
from modules.ext.user import create_user

from modules.schemas.schema_users import RegistrationUser

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token")
async def sign_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    access_token, refresh_token = await authenticate_user(
        form_data.username,
        form_data.password,
        session
    )
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


@router.post("/token/refresh")
async def refresh_token_user():
    pass


@router.post("/registration")
async def sign_up(
    body: RegistrationUser,
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    await create_user(body.username, body.email, body.password, session)
    return "OK"
