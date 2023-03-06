from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis import api_router

app = FastAPI(
    title="API Techgo",
    contact={
        "name": "Huong Pham",
        "github": "https://github.com/huongpx",
    },
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
