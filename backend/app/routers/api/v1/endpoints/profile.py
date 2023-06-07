from typing import Annotated

from fastapi import Depends
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse as R_ORJSON

from sqlalchemy.ext.asyncio import AsyncSession

from routers.api.deps import oauth2_scheme
from routers.api.deps import get_async_session

from modules.schemas.profile import UpdateStatus as UStatus
from modules.schemas.profile import ChangePassword as CPassword

from modules.ext.profile import update_user_status
from modules.ext.profile import change_user_password

from modules.schemas.response.base import DetailResponse

router = APIRouter()

JWTToken = Annotated[str, Depends(oauth2_scheme)]
Session = Annotated[AsyncSession, Depends(get_async_session)]


@router.put("/security/change/password", response_model=DetailResponse, response_class=R_ORJSON)
async def change_password(schema: CPassword, token: JWTToken, session: Session):
    await change_user_password(schema.password, token, session)
    return R_ORJSON({
        "detail": "success"
    })


@router.put("/general/update/status",  response_model=DetailResponse, response_class=R_ORJSON)
async def update_status(scheme: UStatus, token: JWTToken, session: Session):
    await update_user_status(scheme.status, token, session)
    return R_ORJSON({
        "detail": "status updated"
    })
