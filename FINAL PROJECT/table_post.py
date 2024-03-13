from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from table_feed import Feed

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)
    feeds = relationship(Feed)
