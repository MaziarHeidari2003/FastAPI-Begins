from src.books.routes import book_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(book_router,prefix="/books")