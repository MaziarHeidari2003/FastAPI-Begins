from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser | None



class Login(BaseModel):
    password:str
    username:str




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
