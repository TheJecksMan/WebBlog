from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sentry_sdk import init as sentry_init

from core.settings import settings
from routers.api.v1.api import api_router
from modules.database.engine import initialization_database

sentry_init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=1.0,
)

app = FastAPI(
    title=settings.TITLE_APP,
    version=settings.VERSION_APP
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True
)


@app.on_event("startup")
async def startup_event():
    await initialization_database()


app.include_router(api_router, prefix="/api")
