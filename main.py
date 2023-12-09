from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Obtiene la paggina principal
@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item[BaseModel]:
    name: str
    price: float
    is_ofter: bool = None

