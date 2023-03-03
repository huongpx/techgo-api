from schemas.product import (
    CategoryBase,
    Category,
    BrandBase,
    Brand,
    ProductBase,
    Product,
)


class AdminCategoryCreate(CategoryBase):
    pass


class AdminCategoryUpdate(CategoryBase):
    pass


AdminCategory = Category


class AdminBrandCreate(BrandBase):
    pass


class AdminBrandUpdate(BrandBase):
    pass


AdminBrand = Brand


class AdminProductCreate(ProductBase):
    name: str
    category_id: int
    brand_id: int
    description: str


class AdminProductUpdate(ProductBase):
    pass


class AdminProduct(Product):
    pass
