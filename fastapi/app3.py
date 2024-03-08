from fastapi import FastAPI, Query
from datetime import date, timedelta

app = FastAPI()

@app.get("/sum_date")
async def sum_date(current_date: date, offset: int):
    # Вычисляем новую дату, прибавляя offset к current_date
    new_date = current_date + timedelta(days=offset)
    # Возвращаем новую дату в формате YYYY-MM-DD
    return new_date.isoformat()