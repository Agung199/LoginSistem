# MEMBUAT MAIN FASTAPI app
from fastapi import FastAPI, Depends, Session
from app.database import Base, engine
from app.models.user_model import User
from database import get_db
from app.auth import require_admin

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


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return users

@app.get("/admin")
def admin_dashboard(
    current_user: User = Depends(require_admin)
):

    return {
        "message": "Welcome Admin",
        "user": current_user.email,
        "role": current_user.role
    }