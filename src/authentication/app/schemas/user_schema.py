from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool
    is_superuser: bool


class IUserCreate(UserBase):
    password: str

    class Config:
        hashed_password = None


class IUserRead(UserBase):
    hashed_password: str
