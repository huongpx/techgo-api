from pydantic import BaseModel


class CategoryBase(BaseModel):
    id: int | None
    name: str | None


class Category(CategoryBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class AdminCategoryCreate(CategoryBase):
    name: str


class AdminCategoryUpdate(CategoryBase):
    name: str
