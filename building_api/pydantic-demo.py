from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get('/user', response_model=User)
async def get_user():
    return User(id=1, name="John Doe", email="john.doe@example.com")