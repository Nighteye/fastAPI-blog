from fastapi import FastAPI
from blog import schemas

app = FastAPI()

@app.post("/blog")
def create(request: schemas.Blog):
    return {'data': f'Blog is created with title as {request.title} and body as {request.body}'}