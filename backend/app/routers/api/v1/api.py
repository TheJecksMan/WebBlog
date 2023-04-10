from fastapi import APIRouter

from .endpoints.post import router as post_router
from .endpoints.user import router as user_router
from .endpoints.profile import router as profile_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(post_router, prefix="/post", tags=["post"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(profile_router, prefix="/profile", tags=["profile"])
