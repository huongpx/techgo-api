from typing import Any
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from crud.base import CRUDBase
from models.user import User
from schemas import UserCreate, UserUpdate
from core.security import get_password_hash


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        user = db.scalar(stmt)
        return user

    def create(self, db: Session, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            is_staff=obj_in.is_staff,
            is_admin=obj_in.is_admin,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, db_obj: User, obj_in: UserUpdate | dict[str, Any]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True, exclude_none=True)
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db=db, db_obj=db_obj, obj_in=update_data)

    def create_superuser(self, db: Session, email: str, password: str) -> User:
        user = self.get_by_email(db=db, email=email)
        if not user:
            user_in = UserCreate(
                email=email, password=password, is_admin=True, is_staff=True
            )
            user = self.create(db=db, obj_in=user_in)
        return user


user = CRUDUser(User)
