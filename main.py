from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}/{age}")
async def say_hello(name: str, age: int, q: int | None = None):
    return {"message": f"Hello {name}"}

@app.post("/users/")
async def create_user(user: User):
    return {"name": user.name, "age": user.age}
