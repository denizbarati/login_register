from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=['user'])


# Get All Users
@router.get('/')
def get_user():
    return {"message": "all users are here"}
