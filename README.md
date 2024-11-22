# Introduction to FastAPI 
I just started learning FastAPI. Believe it or not, it is really fast!
How long am gonna stick to it? Depends on the job offers!

**Run these two commands as the step zero**
- pip install fastapi
- pip install uvicorn 

Now you can write your first api!

```python

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"name":"Maziar"}

```

**Run this command** 
- uvicorn my-api:app 

**my-api is the name of the file in which my code exists**


**Swagger UI**

This is really cool to get a nice doc on your APIs in the url http://127.0.0.1:8000/docs
