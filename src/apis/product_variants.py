import os

from fastapi import APIRouter, File, UploadFile, HTTPException, status

from utils.constants import IMAGE_TYPES_ALLOWED

router = APIRouter(prefix="/product-variants", tags=["product-variants"])


@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    if not file.content_type in IMAGE_TYPES_ALLOWED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Chỉ cho phép upload định dạng jpeg/png",
        )
    uploaded_file = file.file
    return file.file
