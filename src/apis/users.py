from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from pydantic import EmailStr
from utils.validate import password_strong

from models.user import User
import schemas
import crud
from apis.deps import get_current_user, get_db

# 0: unknown, 1: male, 2: female, 9: not applicable
GENDER_CHOICES = [0, 1, 2, 9]

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


# @router.get("/", tags=["users"])
# async def read_users():
#     return [{"username": "huong"}, {"username": "oanh"}]


@router.get(
    "/me",
    tags=["users"],
    summary="Lấy thông tin user đang đăng nhập",
    response_model=schemas.User,
)
async def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/me", tags=["users"], response_model=schemas.User)
async def update_user_me(
    *,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    firstname: str = Body(None),
    lastname: str = Body(None),
    email: EmailStr = Body(None),
    phone_number: str = Body(None),
    address: str = Body(None),
    gender: int = Body(None),
    password: str = Body(None),
):
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(status_code=400, detail="Email đã tồn tại")
    if not password_strong(password):
        raise HTTPException(
            status_code=400,
            detail="Mật khẩu phải có ít nhất 8 kí tự, bao gồm 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 kí tự đặc biệt",
        )
    if gender not in GENDER_CHOICES:
        raise HTTPException(
            status_code=400,
            detail="Giới tính gửi lên phải là 0 (Không biết), 1 (Nam), 2 (Nữ), 9 (Không cung cấp)",
        )
    user_in = schemas.UserUpdate(
        firstname=firstname,
        lastname=lastname,
        email=email,
        phone_number=phone_number,
        address=address,
        gender=gender,
        password=password,
    )
    user = crud.user.update(db=db, db_obj=current_user, obj_in=user_in)
    return user


# @router.get("/{username}", tags=["users"])
# async def read_user(username: str, age: int = 25):
#     return {"username": username}
