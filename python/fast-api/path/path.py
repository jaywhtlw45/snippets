from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

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
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="sometitle", ge=1)]
):
    return {"item_id":item_id}