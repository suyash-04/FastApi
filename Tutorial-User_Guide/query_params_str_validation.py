from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...): # type: ignore
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q}) # type: ignore
#     return results

# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = ['foo', 'bar']):
#     query_items = {"q": q}
#     return query_items

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#         ),
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q}) # type: ignore
#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q}) # type: ignore
#     return results

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q}) # type: ignore 
    return results