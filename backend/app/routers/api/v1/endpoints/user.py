from typing import Annotated

from fastapi import Query
from fastapi import Depends
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse as R_ORJSON

from sqlalchemy.ext.asyncio import AsyncSession

from routers.api.deps import oauth2_scheme
from routers.api.deps import get_async_session

from modules.ext.user import search_user
from modules.ext.user import current_user

from modules.schemas.response.base import DetailResponse

from modules.schemas.response.user import CurrentUser as CUser


router = APIRouter()

JWTToken = Annotated[str, Depends(oauth2_scheme)]
Session = Annotated[AsyncSession, Depends(get_async_session)]


@router.get(
    "/current",
    response_model=CUser,
    response_class=R_ORJSON,
    responses={
        400: {"model": DetailResponse},
        403: {"model": DetailResponse}
    }
)
async def current_data_user(token: JWTToken, session: Session):
    user = await current_user(token, session)
    return user


@router.post(
    "",
    response_model=CUser,
    response_class=R_ORJSON,
    responses={
        400: {"model": DetailResponse}
    })
async def user_data(
    user_id: Annotated[int, Query(ge=1, le=2**63-1)],
    session: Session
):
    user = await search_user(user_id, session)
    return user
