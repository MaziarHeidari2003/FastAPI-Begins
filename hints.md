#Introduction to FastAPI 

**Run these two commands as the step zero**
- pip install fastapi
- pip install uvicorn 

```python

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"name":"Maziar"}

```

**Run this command** 
- uvicorn my-api:app 

## my-api is the name of the file in which my code exists


**Swagger UI**

This is really cool to get a nice doc on your APIs in the url http://127.0.0.1:8000/docs
