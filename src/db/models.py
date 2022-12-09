from src.db.database import Base
from sqlalchemy import Column, Integer, String


class UserModel(Base):
    __tablename__ = 'users'
    _id = Column(Integer, primary_key=True)
    userName = Column(String)
    password = Column(String)
    email = Column(String)

    @property
    def id(self):
        return self._id
