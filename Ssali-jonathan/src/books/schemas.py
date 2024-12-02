from pydantic import BaseModel
from datetime import date, datetime


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str




class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
