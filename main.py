from fastapi import FastAPI, Query #import fastapi framework
from typing import Union
app = FastAPI()


@app.get("/")
async def root(): # index
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str, skip: int = None, limit: int = 10): # print url an params
    return {"message": f"Hello {name}{skip}{limit}"}

@app.get("/items")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    result = {"items": [{'items_id':"foo"}, {"item_id:""bar"} ]}
    if q:
        result.update({"q": q})
    return result
