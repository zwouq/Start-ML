from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

class PostResponse(BaseModel):
    id: int
    text: str
    topic: str
    
    class Config:
        orm_mode = True

# Функция для подключения к базе данных
def get_db():
    connection = psycopg2.connect(
        database="startml",
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        host="postgres.lab.karpov.courses",
        port=6432,
        cursor_factory=RealDictCursor
    )
    return connection

@app.get("/post/{id}", response_model=PostResponse)
def get_post(id: int, db = Depends(get_db)):
    cur = db.cursor()
    cur.execute(f"""
                SELECT id, text, topic
                FROM "post"
                WHERE id = %s
                """, (id,))
    post = cur.fetchone()
    cur.close()
    db.close()

    if post is None:
        raise HTTPException(status_code=404, detail="post not found")

    return PostResponse(**post)