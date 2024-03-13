from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from table_feed import Feed

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(Integer)
    os = Column(String)
    source = Column(String)
    feeds = relationship(Feed)