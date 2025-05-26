from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    content: str

@app.post("/blog")
def create_blog(request: Blog):
    # Extracting data from the request
    return {request.title: request.content}