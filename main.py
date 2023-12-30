from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    # return "hey...!!"
    # return {"name" : "dev"}    # retun json
    return {"1", "2", "3"}         # retun list


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

# query parameter


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

# /blog/{id}/comments?limit=10&&published=False
# /blog/{id}/comments?limit=10
@app.get('/blog/{id}/comments')
def comments(id, limit=10, published: bool | None = None):
    print(f"id : {id} and published : {published}")
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item

@app.post("/signup")
async def index(request: Request):
    data = await request.json()
    print("signup :: request :: ", data)
    # print("signup :: request :: ",dict(request.receive))
    return "........!!!!???"

# if __name__ == '__main__':                          # this only for development 
#     uvicorn.run("main:app",port=9000,reload=True)

uvicorn.run(app,port=9000)
