from fastapi import APIRouter

router = APIRouter(prefix='/admin', tags=['admin'])


# Get All Admins
@router.get('/')
def get_user():
    return {"message": "all admins are here"}
