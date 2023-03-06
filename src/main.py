from fastapi import FastAPI

from apis import brands, categories, discounts, login, products, users

app = FastAPI()

app.include_router(users.router)
app.include_router(login.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(brands.router)
app.include_router(brands.router)
app.include_router(discounts.router)
