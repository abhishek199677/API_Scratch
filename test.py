from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/abhishek/sunny/abc")
def add(a:int,b:int):
    return a+b



class subtractmodel(BaseModel):
    a: int
    b: int


def subtract(a:int,b:int):
    return a-b

@app.post("/subtract")
def subtract_numbers(model: subtractmodel):
    return subtract(model.a, model.b)
    

print(add(3,4))


# get is not secure the data is exposed itself inisde of the url 
# post is secure the data is not exposed where the data will be exposed in the body
# https://b3462bd13514.ngrok-free.app/abhishek/sunny/abc?a=2&b=2 to run it on ngrok
# http://localhost:8000/abhishek/sunny/abc?a=3&b=5  to run it on postman
# curl "http://localhost:8000/abhishek/sunny/abc?a=3&b=5" to run on command prompt