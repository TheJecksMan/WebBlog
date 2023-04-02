from typing import Annotated

from fastapi import Depends
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse as R_ORJSON

from sqlalchemy.ext.asyncio import AsyncSession

from routers.api.deps import oauth2_scheme
from routers.api.deps import get_async_session

from modules.schemas.profile import ChangePassword as CPassword

from modules.ext.profile import change_user_password


router = APIRouter()

JWTToken = Annotated[str, Depends(oauth2_scheme)]
Session = Annotated[AsyncSession, Depends(get_async_session)]


@router.put("/security/change/password", response_class=R_ORJSON)
async def change_password(schema: CPassword, token: JWTToken, session: Session):
    await change_user_password(schema.password, token, session)
    return {
        "detail": "Success"
    }
