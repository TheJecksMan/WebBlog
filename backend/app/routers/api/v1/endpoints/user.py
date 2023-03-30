from typing import Annotated

from fastapi import Depends
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import ORJSONResponse as R_ORJSON

from sqlalchemy.ext.asyncio import AsyncSession

from routers.api.deps import oauth2_scheme
from routers.api.deps import get_async_session

from modules.ext.user import create_user
from modules.ext.user import update_token
from modules.ext.user import current_user
from modules.ext.user import authenticate_user

from modules.schemas.user import RefreshToken
from modules.schemas.user import RegistrationUser

from modules.schemas.response.user import ResponseToken as RToken
from modules.schemas.response.user import ResponseCurrentUser as RCUser
from modules.schemas.response.user import ResponseRefreshToken as RRToken


router = APIRouter()

Session = Annotated[AsyncSession, Depends(get_async_session)]


@router.post("/token", response_model=RToken, response_class=R_ORJSON)
async def sign_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session
):
    access_token, refresh_token = await authenticate_user(
        form_data.username,
        form_data.password,
        session
    )
    return R_ORJSON({
        "access_token": access_token,
        "refresh_token": refresh_token
    })


@router.post("/token/refresh", response_model=RRToken, response_class=R_ORJSON)
async def refresh_token_user(token: RefreshToken):
    access_token = await update_token(token.refresh_token)
    return R_ORJSON({
        "access_token": access_token
    })


@router.post("/registration", response_class=R_ORJSON)
async def sign_up(
    body: RegistrationUser,
    session: Session
):
    await create_user(body.username, body.email, body.password, session)
    return R_ORJSON({
        "detail": "Success registration!"
    })


@router.get("/me", response_model=RCUser)
async def current_data_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session
):
    user = await current_user(token, session)
    return user
