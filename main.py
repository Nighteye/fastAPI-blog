from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/blog")
def index(limit:int=10, published:bool=True, sort : Optional[str]=None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def show(id:int):
    # fetch blog with id = id
    return {'data': id}

@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    # fetch comments for blog with id = id
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str = "this is a body"
    published_at: Optional[bool] = None

@app.post('/blog')
def createBlog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=9000)