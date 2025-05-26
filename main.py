from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}

# @app.get("/blog/{id}")
# def blog(id: int): #if we don't specify the type, it will be treated as a string
#     return {"blog": id}

@app.get("/blog/{id}")
def blog(id: int):  # 👈 this must be explicitly typed
    return {"blog": id}