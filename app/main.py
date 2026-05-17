# MEMBUAT MAIN FASTAPI app

from fastapi import FastAPI
from app.database import Base, engine
import app.models.user_model

# from app.database import create_user_table
from app.middleware import LoggingMiddleware
from app.routers.auth_router import router as auth_router


app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# @app.on_event("startup")
# def startup():
#    create_user_table()


app.add_middleware(LoggingMiddleware)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "FastApi postgresql Login Api running"}
