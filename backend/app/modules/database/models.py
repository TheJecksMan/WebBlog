from datetime import datetime

from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    reading_time: Mapped[int] = mapped_column(nullable=False)
    create_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    update_at: Mapped[datetime] = mapped_column(nullable=True)


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    avatar_url: Mapped[str] = mapped_column(nullable=True)
    create_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    is_active: Mapped[bool] = mapped_column(default=True)

    role_id: Mapped[int] = mapped_column(ForeignKey("users_role.id"), nullable=False)
    role: Mapped["UsersRole"] = relationship()


class UsersRole(Base):
    __tablename__ = "users_role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(String(7), nullable=False)
