from src.db.database import Base
from sqlalchemy import Column, Integer, String


class UserModel(Base):
    __tablename__ = 'users'
    _id = Column(Integer, primary_key=True)
    userName = Column(String)
    password = Column(String)
    email = Column(String)


class AdminModel(Base):
    __tablename__ = 'admin'
    _id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)
