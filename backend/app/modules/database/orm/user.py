from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from modules.database.models import Users
from modules.database.models import UsersRole


async def get_user(username: str, session: AsyncSession):
    """ Retrieve a user from the database by their username.

    Args:
        username (str): The username to search for.
        session (AsyncSession): An asynchronous session object.

    Returns:
        The first user found with the given username, or None if no user is found.
    """
    result = await session.execute(
        select(Users.id, Users.username, Users.password, Users.is_active, Users.role_id)
        .where(Users.username == username)
    )
    return result.first()


async def insert_user(session: AsyncSession, **kwargs):
    """ Insert a new user into the database.

    Args:
        session (AsyncSession): An asynchronous session object.
        **kwargs: The fields and values to insert into the Users table.

    Returns:
        None
    """
    result = await session.execute(insert(Users).values(**kwargs).returning(Users.id))
    return result.first()


async def update_user(user_id: int, session: AsyncSession, **kwargs):
    """ Update an existing user in the database.

    Args:
        user_id (int): The ID of the user to update.
        session (AsyncSession): An asynchronous session object.
        **kwargs: The fields and values to update in the Users table.

    Returns:
        None
    """
    await session.execute(
        update(Users).values(**kwargs).where(Users.id == user_id)
    )


async def get_current_user(user_id: int, session: AsyncSession):
    """ Retrieve a user from the database by their ID.

    Args:
        user_id (int): The ID of the user whose data is to be retrieved.
        session (AsyncSession): An asynchronous session object.

    Returns:
        The user with the given ID, or None if no user is found.
    """
    result = await session.execute(
        select(
            Users.id, Users.username, Users.avatar_url,  Users.status,
            Users.create_at, Users.is_active,
            UsersRole.name, UsersRole.color
        )
        .join(Users.role)
        .where(Users.id == user_id)
    )
    return result.first()
