from fastapi import APIRouter

from routers.api.v1.endpoints.news import router as news_router
from routers.api.v1.endpoints.user import router as user_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(news_router, prefix="/news", tags=["news"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
