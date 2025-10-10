from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def status():
    return {"status":"Connection Made"}

# @app.get("/items")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q:str | None = None):
#     print("reading")
#     print(q)
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id" : item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q:str | None = None, short:bool = False):
    item = {"item_id": item_id}
    print(short)
    if q:
        item.update({"q":q})
    if not short:
        item.update({
            "description": "very long description"
        })
    return item


# Paramaters can be optional or required. This depends on whether or not a default value is provided to the function paramaters.
# http://localhost:8000/items/mine?q=test-what-happen&short=1