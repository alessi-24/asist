'''
API勉強用
パスパラメータ
'''


from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


'''
特定のユーザーから受け取る場合
先に宣言される必要あり
'''
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


'''
固有値のクラス属性
'''
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


'''
固有値のクラス属性_ver2

input: http://127.0.0.1:8000/physics_great/Albert_Einstein
output: {"greatman_name":"Albert_Einstein","feat":"General and Special theory of relativity "}

'''
class PhysicsName(str, Enum):
    einstein = "Albert_Einstein"
    newton= "Isaac_Newton"
    faraday = "Michael_Faraday"

@app.get("/physics_great/{great_name}")
async def get_model(great_name: PhysicsName):
    if great_name is PhysicsName.einstein:
        return {"greatman_name": great_name, "feat": "General and Special theory of relativity "}

    if great_name is PhysicsName.newton:
        return {"greatman_name": great_name, "feat": "Newtons three laws of motion"}

    if great_name is PhysicsName.faraday:
        return {"greatman_name": great_name, "feat": "Discovery of Electromagnetic Induction"}
