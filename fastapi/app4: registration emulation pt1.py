from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: date

@app.post("/user/validate")
async def validate_user(user: User):
    return {"message": "User data is valid", "user": user}
