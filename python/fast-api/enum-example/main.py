from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()
print("Succesfully created enum")
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
print(fake_items_db)

@app.get("/")
async def root():
    return {"status": "connection successful"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    newModel = ModelName("alexnet")
    print(newModel)

    if model_name is ModelName.alexnet:
        return {"model_name":model_name, "message":"deeplearning"}
    if model_name.value == "lenet":
        return {"model_name":"lenet", "message":"lecnn all the images"}
    return {"model_name":model_name, "message":"residuals"}


