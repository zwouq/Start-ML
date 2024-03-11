from database import Base, engine, SessionLocal
from sqlalchemy import Column, Integer, String

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = SessionLocal()

    business_posts = session.query(Post.id).filter(Post.topic == "business").order_by(Post.id.desc()).limit(10).all()
    business_post_ids = [post.id for post in business_posts]
    print(business_post_ids)


