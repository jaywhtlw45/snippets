from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

app.get("/")
async def status():
    return {"status": "test.py"}

app.get("/item")
async def read_item(q: Annotated[str, Query(max_length=50)] = "querrystring"):
    return "success"