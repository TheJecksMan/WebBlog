from fastapi import APIRouter

from routers.api.v1.endpoints.post import router as post_router
from routers.api.v1.endpoints.user import router as user_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(post_router, prefix="/post", tags=["post"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
