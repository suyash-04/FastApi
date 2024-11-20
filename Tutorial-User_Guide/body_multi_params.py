from typing import Annotated 
from fastapi import FastAPI , Path , Body
from pydantic import BaseModel
 
app = FastAPI()

class Item(BaseModel):
    name : str
    description : str | None = None 
    price : float 
    tax : float | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id : Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)], 
#     q : str | None = None,
#     item : Item | None = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q}) # type: ignore
#     if item:
#         results.update({"item" : item}) # type: ignore
#     return results

# # class User(BaseModel):
#     username: str
#     full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, item: Item, user: User, importance: Annotated[int, Body() , q : str | None = None]
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results