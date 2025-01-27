from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import models, schemas, hash
from .database import engine
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas
from typing import List
from .routers import blog, user,authentication

# session is not a pydantic thing so we have to use depends

app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)


# this bcrypt asshole differs from sha256

"""
what is pep8(python enhancement proposal) in python?
it is a style guide for pyhton code that provides recomendations for code formatting and organizations

"""

