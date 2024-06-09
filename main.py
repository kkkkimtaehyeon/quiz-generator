from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain import upload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload")


