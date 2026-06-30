from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str = "this is a body"
