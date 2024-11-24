from fastapi import FastAPI
from typing import Optional
# import uvicorn

app = FastAPI()

@app.get('/')
def index(limit:int = 10,published:bool = True,sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from the db'}
    
    else:
        return {'data':f'{limit} blogs from db'}
   


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


# the sequence of the routes matters

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


# you can see the path param in two places, one in the decorator and one in the method args
# but you can only see the queryparam in the method arg

#to declare the request body you need to use the pydantice module

from pydantic import BaseModel
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post('/blog')
def create_blog(request:Blog):
    return {f'blog is created as {request.title}'}


# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port='9000')