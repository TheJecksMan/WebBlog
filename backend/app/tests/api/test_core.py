import jwt

from datetime import datetime, timedelta

from tests.modules.contsants import TEST_PASSWORD_PLAINTEXT
from core.settings import settings

from core.security import get_password_hash, verify_password
from core.jwt import generate_token, update_access_token


def test_hashed_password():
    hashed_password = get_password_hash(TEST_PASSWORD_PLAINTEXT)
    isVerify = verify_password(TEST_PASSWORD_PLAINTEXT, hashed_password)
    assert isVerify


def test_jwt_encode():
    user_id, role_id = 1, 3

    acc_token, rf_token = generate_token(user_id, role_id)

    result = jwt.decode(acc_token, settings.SECRET_ACCESS_TOKEN, 'HS256')

    assert result["user_id"] == user_id
    assert result["role_id"] == role_id

    result = jwt.decode(rf_token, settings.SECRET_REFRESH_TOKEN, 'HS256')

    assert result["user_id"] == user_id
    assert result["role_id"] == role_id


def test_jwt_update():
    user_id, role_id = 1, 3

    _, rf_token = generate_token(user_id, role_id)
    acc_token = update_access_token(rf_token)

    result = jwt.decode(acc_token, settings.SECRET_ACCESS_TOKEN, 'HS256')

    assert result["user_id"] == user_id
    assert result["role_id"] == role_id
