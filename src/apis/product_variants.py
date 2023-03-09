import os
import secrets

from fastapi import APIRouter, File, UploadFile, HTTPException, status
from PIL import Image

from utils.constants import IMAGE_TYPES_ALLOWED

router = APIRouter(prefix="/product-variants", tags=["product-variants"])


@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    if not file.content_type in IMAGE_TYPES_ALLOWED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Chỉ cho phép upload định dạng jpeg/png",
        )
    img = Image.open(file.file)
    img_out_size = (512, 512)
    img.thumbnail(img_out_size)

    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(file.filename)  # type: ignore
    image_fn = random_hex + f_ext  # type: ignore
    to_save_path = os.path.join("media/product_images", image_fn)
    img.save(to_save_path)
    img.close()

    return "/files/" + image_fn
