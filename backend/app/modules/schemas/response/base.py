from pydantic import BaseModel

from core.orjson import orjson_dumps


class DetailResponse(BaseModel):
    detail: str

    class Config:
        json_dumps = orjson_dumps
