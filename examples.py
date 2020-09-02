from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):
    name: str
    price: str
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
def read_test():
    return {"text": "this is a test"}


@app.put("/update/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}
