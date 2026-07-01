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
    class Config():
        from_attributes = True


class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser
    class Config():
        from_attributes = True