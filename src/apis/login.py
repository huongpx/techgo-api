from typing import Any

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

import schemas
from apis.deps import get_db
from models.user import User
from utils import password_strong, create_access_token
from core.security import verify_password, get_password_hash


router = APIRouter(tags=["login"])


@router.post("/login/access-token")
async def login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """Login API"""
    stmt = select(User).where(User.email == form_data.username)
    user = db.scalar(stmt)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Authenticate failed",
        )
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Authenticate failed",
        )
    return {"access_token": create_access_token(user.email), "token_type": "bearer"}


@router.post("/register", response_model=schemas.User)
async def register(
    db: Session = Depends(get_db), *, user_data: schemas.UserCreate
) -> Any:
    """Register API"""
    stmt = select(User).where(User.email == user_data.email)
    user = db.scalar(stmt)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist",
        )
    if not password_strong(user_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password is too weak",
        )
    hashed_password = get_password_hash(user_data.password)
    new_user = User(email=user_data.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return new_user
