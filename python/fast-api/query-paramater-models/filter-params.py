from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)        # skip the first offset of items
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


# filter_query is unpacked to allow multiple querries to be made. Query causes this behavior
# GET /items/?limit=50&offset=10&order_by=updated_at&tags=python&tags=fastapi&tags=web HTTP/1.1
@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

