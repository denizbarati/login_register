from sqlalchemy.orm.session import Session
from src.db import models
from src.db import schemas


async def create_user(db: Session, request: schemas.UserBase):
    user = models.UserModel(
        userName=request.user_name,
        password=request.password,
        email=request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
