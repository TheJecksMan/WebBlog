from fastapi import FastAPI

from routers.api.v1.api import api_router

from modules.database.engine import initialization_database


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await initialization_database()


app.include_router(api_router, prefix="/api")
