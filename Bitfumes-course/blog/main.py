from fastapi import FastAPI 
from .schemas import Blog

app = FastAPI()



@app.post('/blog')
def create(request: Blog):
    return request
# now we dont really call these args query params , maybe becausse it is a post method
