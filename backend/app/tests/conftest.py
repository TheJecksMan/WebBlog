import pytest
from httpx import AsyncClient

from main import app

from modules.database.engine import async_session

DEFAULT_PATH = "http://127.0.0.1:8000"


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.fixture
async def session():
    async with async_session.begin() as session:
        yield session


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url=DEFAULT_PATH) as client:
        yield client
