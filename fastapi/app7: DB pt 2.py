from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Функция для подключения к базе данных
def get_db_connection():
    connection = psycopg2.connect(
        database="startml",
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        host="postgres.lab.karpov.courses",
        port=6432
    )
    return connection

@app.get("/user/{user_id}")
def read_user(user_id: int):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""
                SELECT gender, age, city
                FROM "user"
                WHERE id = %s
                """, (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user is None:
        raise HTTPException(status_code=404, detail="user not found")

    return user