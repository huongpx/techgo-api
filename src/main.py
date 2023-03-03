from fastapi import FastAPI
from sqladmin import Admin, ModelView

from apis import login, users, products, admin_categories
from db.session import engine
from models.product import Category, Product, ProductVariant
from models.user import User

app = FastAPI()

app.include_router(users.router)
app.include_router(login.router)
app.include_router(products.router)
app.include_router(admin_categories.router)
