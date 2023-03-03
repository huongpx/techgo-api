from crud.base import CRUDBase
from schemas import AdminCategoryCreate, AdminCategoryUpdate
from models.product import Category


class CRUDCategory(CRUDBase[Category, AdminCategoryCreate, AdminCategoryUpdate]):
    pass


category = CRUDCategory(Category)
