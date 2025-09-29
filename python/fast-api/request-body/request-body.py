from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/")
async def status():
    return {"status":"connection established request-body"}

# @app.post("/item")
# async def create_item(item: Item):
#     item_dict : dict = item.model_dump()
#     print(item_dict)

#     response: dict = { "message": "successfully created item"}
#     response.update(item)
#     return response

# @app.put("/item/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id":item_id, **item.model_dump()}

@app.put("/item/{item_id}")
async def update_item(item_id:int, item: Item, q:str | None = None):
    result = {"item:id" : item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

