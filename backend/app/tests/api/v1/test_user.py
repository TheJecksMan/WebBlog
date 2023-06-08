import pytest

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from tests.modules.utils import random_email
from tests.modules.utils import random_lowercase_string

from modules.database.orm.user import get_user


@pytest.mark.anyio
async def test_correct_create_user(client: AsyncClient, session: AsyncSession):
    email = random_email(10)
    username = random_lowercase_string(20)
    password = random_lowercase_string(20)

    data = {"email": email, "username": username, "password": password}

    res = await client.post(url="api/v1/auth/registration", json=data)
    assert res.status_code == 200

    user = await get_user(username, session)
    assert user.is_active
    assert user.username == username


@pytest.mark.anyio
async def test_uncorrect_create_user(client: AsyncClient):
    email = random_email(350)
    username = random_lowercase_string(20)
    password = random_lowercase_string(20)

    data = {"email": email, "username": username, "password": password}

    res = await client.post(url="api/v1/auth/registration", json=data)
    assert res.status_code == 422


@pytest.mark.anyio
async def test_existing_create_user(client: AsyncClient):
    email = random_email()
    username = random_lowercase_string(20)
    password = random_lowercase_string(20)

    data = {"email": email, "username": username, "password": password}
    res = await client.post(url="api/v1/auth/registration", json=data)
    assert res.status_code == 200

    res = await client.post(url="api/v1/auth/registration", json=data)
    assert res.status_code == 400
