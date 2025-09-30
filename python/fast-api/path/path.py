from fastapi import FastAPI, Path, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def status():
    return { "status":"path.py"}

# @app.post("/item/{item_id}")
# async def create_item(item: Item):
#     return item

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", alias="other-item")],x
#     q: Annotated[str | None, Query(alias = "item-qeury")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results


## greater than or equal to
# ge gt le lt
# greater than, less than or equal, less than
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="sometitle", ge=1)]
# ):
#     return {"item_id":item_id}