from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from database import Base
from table_user import User
from table_post import Post

class Feed(Base):
    __tablename__ = "feed_action"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    action = Column(String)
    time = Column(DateTime)