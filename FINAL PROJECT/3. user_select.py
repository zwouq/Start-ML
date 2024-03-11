from database import Base, engine, SessionLocal
from sqlalchemy import Column, Integer, String, func

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

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = SessionLocal()

user_3_group = session.query(
    User.country,
    User.os,
    func.count('*').label('user_count')
).filter(
    User.exp_group == 3
).group_by(
    User.country,
    User.os
).having(
    func.count('*') > 100
).order_by(
    func.count('*').desc()
).all()
user_3_group_list = [(user.country, user.os, user.user_count) for user in user_3_group]
print(user_3_group_list)