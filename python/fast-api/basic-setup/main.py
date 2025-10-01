from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_items(item_id : int):
    return { "item_id" : item_id}

@app.get("/items/{item_id}/{q}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# Coroutine is just the very fancy term for the thing returned by an async def function, comparable to Goroutines in Go
# !! Pay attention to the order of routes. they are evaluated top to bottom so routes that use /someroute and /{id} the /someroute needs to come first