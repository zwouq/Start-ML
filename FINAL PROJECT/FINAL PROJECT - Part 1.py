from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from sqlalchemy.sql import func
from database import SessionLocal
from table_post import Post
from table_feed import Feed
from schema import PostGet
from typing import List

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/post/recommendations/", response_model=List[PostGet])
def get_recommended_feed(limit: int = Query(default=10, ge=1), db: Session = Depends(get_db)):
    top_posts = (
    db.query(Post.id, Post.text, Post.topic, func.count(Feed.post_id).label('likes'))
    .join(Feed, Post.id == Feed.post_id)  # Join Post and Feed on post ID
    .filter(Feed.action == 'like')  # Filter actions for 'like'
    .group_by(Post.id)  # Group by Post ID
    .order_by(func.count(Feed.post_id).desc())  # Order by like count in descending order
    .limit(limit)  # Apply limit to results
    .all()  # Fetch all results within the limit
    )
    return top_posts
