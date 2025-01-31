from sqlmodel import SQLModel,Field,Column
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
import uuid

class Book(SQLModel,table=True):
    __tablename__ = 'bookds'
    uid: uuid.UUID=Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default = uuid.uuid4()
        )
    )
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at = datetime
    updated_at = datetime
