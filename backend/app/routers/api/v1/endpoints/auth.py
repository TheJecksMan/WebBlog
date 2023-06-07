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
from modules.ext.user import authenticate_user

from modules.schemas.user import RefreshToken
from modules.schemas.user import RegistrationUser

from modules.schemas.response.base import DetailResponse

from modules.schemas.response.user import Token
from modules.schemas.response.user import IDUser
from modules.schemas.response.user import AccessToken as AToken


router = APIRouter()

JWTToken = Annotated[str, Depends(oauth2_scheme)]
FormLogin = Annotated[OAuth2PasswordRequestForm, Depends()]
Session = Annotated[AsyncSession, Depends(get_async_session)]


@router.post(
    "/token",
    response_class=R_ORJSON,
    responses={
        200: {"model": Token},
        400: {"model": DetailResponse},
        403: {"model": DetailResponse}
    })
async def sign_in(form_data: FormLogin, session: Session):
    access_token, refresh_token = await authenticate_user(
        form_data.username,
        form_data.password,
        session
    )
    return R_ORJSON({
        "access_token": access_token,
        "refresh_token": refresh_token
    })


@router.post(
    "/token/refresh",
    response_class=R_ORJSON,
    responses={
        200: {"model": AToken},
        400: {"model": DetailResponse}
    })
async def refresh_token_user(token: RefreshToken):
    access_token = await update_token(token.refresh_token)
    return R_ORJSON({
        "access_token": access_token
    })


@router.post(
    "/registration",
    response_class=R_ORJSON,
    responses={
        200: {"model": IDUser},
        400: {"model": DetailResponse}
    })
async def sign_up(body: RegistrationUser, session: Session):
    user_id = await create_user(body.username, body.email, body.password, session)
    return R_ORJSON({
        "user_id": user_id
    })
