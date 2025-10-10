# from enum import Enum
# from fastapi import FastAPI

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# app = FastAPI()
# print("Succesfully created enum")

# @app.get("/")
# async def root():
#     return {"status": "connection successful"}

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name":model_name, "message":"deeplearning"}
#     if model_name.value == "lenet":
#         return {"model_name":"lenet", "message":"lecnn all the images"}
#     return {"model_name":model_name, "message":"residuals"}


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
    return {"Connection": "Established"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}