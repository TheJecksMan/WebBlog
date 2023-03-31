import pytest

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from tests.test_modules.utils import random_email
from tests.test_modules.utils import random_lowercase_string

from modules.database.orm.user import get_user_by_username


@pytest.mark.anyio
async def test_correct_create_user(client: AsyncClient, session: AsyncSession):
    email = random_email()
    username = random_lowercase_string(20)
    password = "$2a$12$wwZhYsm/IJpjJjY5xlXY5eogwvstUvB0Nq8zkRhqsJghr8OeWtiqy"

    data = {"email": email, "username": username, "password": password}

    res = await client.post(url="/api/v1/user/registration", json=data)
    assert res.status_code == 200

    user = await get_user_by_username(username, session)
    assert user.is_active == True
    assert user.username == username


@pytest.mark.anyio
async def test_uncorrect_create_user(client: AsyncClient):
    email = random_email(350)
    username = random_lowercase_string(20)
    password = "$2a$12$wwZhYsm/IJpjJjY5xlXY5eogwvstUvB0Nq8zkRhqsJghr8OeWtiqy"

    data = {"email": email, "username": username, "password": password}

    res = await client.post(url="/api/v1/user/registration", json=data)
    assert res.status_code == 422


@pytest.mark.anyio
async def test_existing_create_user(client: AsyncClient):
    email = random_email()
    username = random_lowercase_string(20)
    password = "$2a$12$wwZhYsm/IJpjJjY5xlXY5eogwvstUvB0Nq8zkRhqsJghr8OeWtiqy"

    data = {"email": email, "username": username, "password": password}
    res = await client.post(url="/api/v1/user/registration", json=data)
    assert res.status_code == 200

    res = await client.post(url="/api/v1/user/registration", json=data)
    assert res.status_code == 400
