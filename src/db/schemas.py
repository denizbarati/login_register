from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str
    password: str
    email: str
