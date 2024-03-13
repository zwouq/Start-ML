from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from table_user import User
from table_post import Post
from table_feed import Feed
from schema import UserGet, PostGet, FeedGet
from typing import List

app = FastAPI()

# Dependency function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db    # yield the database session to the route handler
    finally:
        db.close()  # close the session after the route handler finishes

@app.get("/user/{id}", response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Route to get a user by ID
@app.get("/post/{id}", response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")   # raise an HTTP 404 error if the post is not found
    return post

# Route to get a user's feed
@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    feed = db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()
    if not feed:
        return []   # return an empty list if the feed is empty
    return [{"user_id": item.user_id, "post_id": item.post_id, "action": item.action, "time": item.time} for item in feed]

# Route to get a post's feed
@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    feed = db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()
    if not feed:
        return []   # return an empty list if the feed is empty
    return [{"user_id": item.user_id, "post_id": item.post_id, "action": item.action, "time": item.time} for item in feed]