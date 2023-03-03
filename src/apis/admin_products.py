from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from apis.deps import get_current_admin, get_db

import schemas, crud

router = APIRouter(prefix="/admin/products")


@router.post(
    "/",
    response_model=schemas.Product,
    dependencies=[Depends(get_current_admin)],
    summary="Tạo sản phẩm mới (chỉ admin)",
)
async def create_product(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.ProductCreate,
):
    item = crud.product.create(db=db, obj_in=obj_in)
    return item


@router.put("/{id}", response_model=schemas.Product)
async def update_product(
    *, db: Session = Depends(get_db), id: int, product_in: schemas.ProductUpdate
):
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    product = crud.product.update(db=db, db_obj=product, obj_in=product_in)
    return product


@router.delete("/{id}", response_model=schemas.Product)
async def delete_product(*, db: Session = Depends(get_db), id: int):
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    product = crud.product.remove(db=db, db_obj=product)
    return product
