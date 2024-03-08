from fastapi import FastAPI
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
    # Формируем строку с информацией о пользователе для ответа
    response_message = f"Will add user: {user.name} {user.surname} with age {user.age}"
    # Возвращаем строку с информацией о пользователе
    return response_message
