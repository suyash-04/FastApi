from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel , HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl # The string will be checked to be a valid URL, and documented in JSON Schema / OpenAPI as such.
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image:list[Image] | None = None
# tags : set[str] : set() ##for items to be unique 


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results




@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
