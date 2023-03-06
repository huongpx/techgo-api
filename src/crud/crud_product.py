from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.product import Brand, Category, Discount, Product, ProductVariant
from schemas import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def get_multi_filter(
        self,
        db: Session,
        category_id: int | None = None,
        brand_id: int | None = None,
        keyword: str | None = None,
        skip: int = 0,
        limit: int = 10,
    ) -> Sequence[Product]:
        stmt = select(Product)
        if category_id:
            stmt = stmt.where(Product.category_id == category_id)
        if brand_id:
            stmt = stmt.where(Product.brand_id == brand_id)
        if keyword:
            stmt = stmt.where(Product.name.icontains(keyword))
        stmt = stmt.offset(skip).limit(limit)
        items = db.scalars(stmt).all()
        return items


product = CRUDProduct(Product)
