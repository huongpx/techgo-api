from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class BrandBase(BaseModel):
    name: str


class Brand(BrandBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str | None
    category_id: int | None
    brand_id: int | None
    description: str | None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Product(ProductBase):
    id: int
    name: str
    category_id: int
    brand_id: int
    description: str

    class Config:
        orm_mode = True
