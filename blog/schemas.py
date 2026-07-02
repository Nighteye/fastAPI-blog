from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title: str = "this is a title"
    body: str = "this is a body"


class User(BaseModel):
    name: str
    email: str
    password: str        


class ShowUser(BaseModel):
    name: str
    email: str
    blogs : List[Blog] = []


class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser