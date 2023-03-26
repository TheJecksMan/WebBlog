from fastapi import APIRouter

from routers.api.v1.endpoints.news import router as news_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(news_router, prefix="/news", tags=["news"])
