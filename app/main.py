# MEMBUAT MAIN FASTAPI app

from fastapi import FastAPI
from app.database import create_user_table
from app.middleware import LogingMiddleware
from app.routers.auth_router import router as auth_router

create_user_table()

app = FastAPI()

app.add_middleware(LogingMiddleware)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "FastApi SQlite Login Api running"}
