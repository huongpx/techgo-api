from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
from apis.deps import get_db, get_current_admin
import schemas

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[schemas.Product], summary="Lấy danh sách sản phẩm")
async def read_products(
    *,
    db: Session = Depends(get_db),
    category_id: int | None = None,
    brand_id: int | None = None,
    keyword: str | None = None,
    skip: int = 0,
    limit: int = 10,
):
    """
    Các tham số: truyền tham số dạng ?skip=0&limit=10...
    - Phân trang:
        - skip: để phân trang, vd trang 1 thì skip = 0, trang 2 thì skip = 1 * limit
        - limit: số sản phẩm trong 1 trang
    - Tìm kiếm:
        - keyword: để tìm kiếm theo tên sản phẩm
        - category_id: truyền id của danh mục sản phẩm
        - brand_id: id của thương hiệu
    """
    products = crud.product.get_multi_filter(
        db=db,
        category_id=category_id,
        brand_id=brand_id,
        keyword=keyword,
        skip=skip,
        limit=limit,
    )
    return products


@router.get(
    "/{id}",
    response_model=schemas.Product,
    dependencies=[Depends(get_current_admin)],
    summary="Xem sản phẩm",
)
async def read_product(*, db: Session = Depends(get_db), id: int):
    product = crud.product.get(db=db, id=id)
    return product
