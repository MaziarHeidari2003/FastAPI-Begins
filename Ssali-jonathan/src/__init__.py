from src.books.routes import book_router
from fastapi import FastAPI
from contextlib import  asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting...")
    await init_db()

    yield
    print("The server has been stopped")


    """
    What is yield?
yield is a keyword in Python used in the context of generators and context managers. It allows a function to:

Pause execution and return a value to the caller.
Later, resume execution from where it left off.
When used with the @asynccontextmanager decorator, yield divides the function into two phases:

Before yield: Code executed during the setup phase (e.g., initializing resources).
After yield: Code executed during the teardown phase (e.g., cleaning up resources).
    """

version = "v1"


app = FastAPI(
    title='Bookly',
    description="A REST API  for a book review service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router,prefix="/api/{version}/books",tags=['books'])