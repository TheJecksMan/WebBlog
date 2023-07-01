from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from core.settings import settings
from routers.api.v1.api import api_router
from modules.database.engine import initialization_database


if settings.ENABLE_SENTRY:
    from sentry_sdk import init as sentry_init

    sentry_init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        debug=settings.DEBUG_MODE
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    await initialization_database()
    yield

app = FastAPI(
    title=settings.TITLE_APP,
    version=settings.VERSION_APP,
    lifespan=lifespan,
    default_response_class=ORJSONResponse
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True
)

app.include_router(api_router, prefix="/api")
