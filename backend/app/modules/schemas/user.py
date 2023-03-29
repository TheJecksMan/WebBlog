from pydantic import BaseModel
from pydantic import EmailStr


class RegistrationUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class RefreshToken(BaseModel):
    refresh_token: str
