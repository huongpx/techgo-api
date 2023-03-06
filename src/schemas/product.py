from pydantic import BaseModel

from schemas.category import Category
from schemas.brand import Brand


class ProductBase(BaseModel):
    name: str | None
    category_id: int | None
    brand_id: int | None
    description: str | None


class ProductCreate(ProductBase):
    name: str
    category_id: int
    brand_id: int
    description: str


class ProductUpdate(ProductBase):
    pass


class Product(BaseModel):
    id: int
    name: str
    category: Category
    brand: Brand
    description: str

    class Config:
        orm_mode = True
