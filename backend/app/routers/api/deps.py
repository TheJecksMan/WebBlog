from fastapi.security import OAuth2PasswordBearer

from modules.database.engine import async_session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/user/token")


async def get_async_session():
    async with async_session.begin() as session:
        yield session
