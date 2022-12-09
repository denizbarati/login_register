from fastapi import APIRouter, Depends
from src.services import users
from src.db.schemas import UserBase
from src.db.database import get_db

router = APIRouter(prefix='/user', tags=['user'])


@router.post('/creat')
async def creat_user(user: UserBase, db=Depends(get_db)):
    return await users.create_user(db, user)


@router.get('/')
async def get_all_users(db=Depends(get_db)):
    return await users.get_all_users(db)


@router.get('/get/{id}')
async def get_user_by_id(id: int, db=Depends(get_db)):
    return await users.get_user_by_id(id, db)


@router.get('/delete/{id}')
async def delete_user_by_id(id: int, db=Depends(get_db)):
    return await users.delete_user(id, db)


@router.post('/update/{id}')
async def update_user_by_id(user: UserBase, id: int, db=Depends(get_db)):
    return await users.update_user(db, user, id)
