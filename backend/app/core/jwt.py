import jwt
import datetime

from typing import Tuple
from typing import Optional

from jwt.exceptions import PyJWTError

from core.settings import settings


def generate_token(user_id: int) -> Tuple[str, str]:
    """Generate new JSON Web Token (RFC 7519) for user.
    """
    access_token_expires = datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRED)
    refresh_token_expires = datetime.timedelta(days=settings.REFRESH_TOKEN_EXPIRED)

    # Create access token
    access_token_payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + access_token_expires,
        "iat": datetime.datetime.utcnow()
    }
    access_token = jwt.encode(
        access_token_payload,
        settings.SECRET_ACCESS_TOKEN,
        algorithm="HS256"
    )

    # Create refresh token
    refresh_token_payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + refresh_token_expires,
        "iat": datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload,
        settings.SECRET_REFRESH_TOKEN,
        algorithm="HS256"
    )
    return access_token, refresh_token


def update_access_token(refresh_token: str) -> Optional[str]:
    """Updating the access token if it has expired.
    """
    # Decode the refresh token to get the user ID
    try:
        refresh_token_payload = jwt.decode(
            refresh_token,
            settings.SECRET_REFRESH_TOKEN,
            algorithms=["HS256"]
        )
    except PyJWTError:
        # Handle expired tokens
        return None

    # Create a new access token
    user_id = refresh_token_payload["user_id"]
    access_token_expires = datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRED)
    access_token_payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + access_token_expires,
        "iat": datetime.datetime.utcnow()
    }
    access_token = jwt.encode(
        access_token_payload,
        settings.SECRET_ACCESS_TOKEN,
        algorithm="HS256"
    )
    return access_token


def get_user_id_token(access_token: str) -> Optional[int]:
    """ Get user_id on jwt payload. If it has valid.
    """
    # Decode the refresh token to get the user ID
    try:
        access_token_payload = jwt.decode(
            access_token,
            settings.SECRET_ACCESS_TOKEN,
            algorithms=["HS256"]
        )
    except PyJWTError:
        # Handle expired tokens
        return None

    user_id = access_token_payload["user_id"]
    return user_id
