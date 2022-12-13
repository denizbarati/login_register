from fastapi import APIRouter

router = APIRouter(prefix='/admin', tags=['admin'])


# Get All Admins
@router.get('/login')
def get_user():
    # generate token here
    return {"message": "all admins are here"}
