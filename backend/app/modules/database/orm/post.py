from sqlalchemy import func
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from modules.database.models import Posts
from modules.database.models import Users


async def create_post(session: AsyncSession, **kwargs) -> int:
    """ Creates a new post in the database with the provided data.

    Args:
        session (AsyncSession): An asynchronous session object.
        **kwargs: Keyword arguments containing the data to be inserted into the Posts table.

    Returns:
        The ID of the newly created post.
    """
    smt = insert(Posts).values(**kwargs).returning(Posts.id)

    result = await session.execute(smt)
    return result.first()[0]


async def update_post(post_id: int, session: AsyncSession, **kwargs) -> int:
    """ Updates an existing post in the database with the provided data.

    Args:
        post_id (int): The ID of the post to be updated.
        session (AsyncSession): An asynchronous session object.
        **kwargs: Keyword arguments containing the data to be updated in the Posts table.

    Returns:
        The ID of the updated post.
    """
    smt = update(Posts).where(Posts.id == post_id).values(**kwargs)\
        .returning(Posts.id)

    result = await session.execute(smt)
    return result.first()[0]


async def get_post(post_id: int, session: AsyncSession):
    """ Retrieves a single post from the database with the provided ID.

    Args:
        post_id (int): The ID of the post to be retrieved.
        session (AsyncSession): An asynchronous session object.

    Returns:
        The requested post data.
    """
    smt = select(Posts.id, Posts.title, Posts.text, Posts.create_at,
                 Users.username, Posts.reading_time)\
        .join(Users)\
        .where(Posts.id == post_id)

    result = await session.execute(smt)
    return result.first()


async def get_multiply_post(posts_id: int, limit: int, session: AsyncSession):
    """ Retrieves multiple posts from the database
    with IDs greater than the provided ID.

    Args:
        posts_id (int): The ID of the most recent post to exclude from the results.
        limit (int): The maximum number of posts to retrieve.
        session (AsyncSession): An asynchronous session object.

    Returns:
        A list of the requested post data.
    """
    smt = select(Posts.id, Posts.create_at, Posts.title, Users.username, Posts.reading_time)\
        .join(Users)\
        .where(Posts.id > posts_id)\
        .order_by(Posts.create_at.desc())\
        .limit(limit)

    result = await session.execute(smt)
    return result.all()


async def get_multiply_posts_user(user_id: int, posts_id: int, limit: int, session: AsyncSession):
    """ Retrieves multiple posts from the database
    with IDs greater than the provided ID and authored by the provided user.

    Args:
        user_id (int): The ID of the user who authored the posts.
        posts_id (int): The ID of the most recent post to exclude from the results.
        limit (int): The maximum number of posts to retrieve.
        session (AsyncSession): An asynchronous session object.

    Returns:
        A list of the requested post data.
    """
    smt = select(Posts.id, Posts.create_at, Posts.title)\
        .join(Users)\
        .where(Posts.id > posts_id, Posts.author == user_id)\
        .order_by(Posts.create_at.desc())\
        .limit(limit)

    result = await session.execute(smt)
    return result.all()


async def delete_post(post_id: int, session: AsyncSession) -> int:
    """ Deleting a requested post by its ID

    Args:
        post_id (int): The ID of the post you want to remove.
        session (AsyncSession): An asynchronous session object.

    Returns:
        The requested post data.
    """
    smt = delete(Posts).where(Posts.id == post_id).returning(Posts.id)

    result = await session.execute(smt)
    return result.first()[0]


async def get_count_post(session: AsyncSession):
    """ Retrieves the total number of posts used for pagination.

    Args:
        session (AsyncSession): An asynchronous session object.

    Returns:
        Total number of posts.
    """
    smt = select(func.count(Posts.id))

    result = await session.execute(smt)
    return result.first()


async def get_count_posts_user(user_id: int, session: AsyncSession):
    """ Retrieves the number of user posts.

    Args:
        user_id (int): The ID of the user whose post count data is to be retrieved.
        session (AsyncSession): An asynchronous session object.

    Returns:
        Total number of posts.
    """
    smt = select(func.count(Posts.id)).where(Posts.author == user_id)

    result = await session.execute(smt)
    return result.first()
