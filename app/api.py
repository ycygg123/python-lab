from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    quantity: int = 1


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"hello": name}


@app.get("/add/{a}/{b}")
def add_two_nums(a: int, b: int):
    return {"result": a + b}


@app.post("/items")
def create_item(item: Item):
    return {"name": item.name, "price": item.price, "total": item.price * item.quantity}
