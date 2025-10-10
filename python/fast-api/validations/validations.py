import random
from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import AfterValidator
app = FastAPI()

@app.get("/")
async def status():
    return {"connection": "validations.py"}

# @app.get("/items")
# async def read_items(q: Annotated[str|None, Query(max_length=10)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results

# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query(title="i am a title", description="i am a description", max_length=1)]):
#     query_items = {"q": q}
#     return query_items

### Custom Valiation
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}

    
