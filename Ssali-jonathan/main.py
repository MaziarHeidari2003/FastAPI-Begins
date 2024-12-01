from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
async def read_root():
    return {"msg":"hello world"}

@app.get('/greet/{name}')
def greet_name(name:Optional[str]='User', age: int= 0) -> dict:
    return {"message":f"Hello {name} age:{age}"}