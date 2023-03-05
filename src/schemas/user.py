from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    """Shared props received via API on update"""

    firstname: str | None
    lastname: str | None
    email: EmailStr | None
    phone_number: str | None
    address: str | None
    gender: int | None
    is_admin: bool | None
    is_staff: bool | None


class UserCreate(UserBase):
    """Props received via API on create"""

    email: EmailStr
    password: str


class UserUpdate(UserBase):
    """Props received via API on update"""

    password: str | None


class UserInDBBase(UserBase):
    id: int | None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    """Properties to return via API"""

    pass


class UserInDB(UserInDBBase):
    """Properties stored in DB"""

    hashed_password: str
