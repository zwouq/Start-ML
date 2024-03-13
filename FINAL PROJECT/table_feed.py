from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from database import Base
from table_user import User
from table_post import Post
from sqlalchemy.orm import relationship

class Feed(Base):
    __tablename__ = "feed_action"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    action = Column(String)
    time = Column(DateTime)
    