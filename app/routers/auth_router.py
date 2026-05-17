# MEMBUAT ROUTER AUTHENTICATION
from fastapi import APIRouter
from fastapi import HTTPException, Depends

# from app.database import get_connection
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User

from app.schemas import RegisterSchema
from app.schemas import LoginSchema

from app.auth import hash_password
from app.auth import verify_password
from app.auth import create_access_token

# import sqlite3

# membuat Endpoint profile
from app.auth import get_current_user

router = APIRouter()


# from app.database import get_connection


# REGISTER
@router.post("/register")
def register(user: RegisterSchema, db: Session = Depends(get_db)):

    # cek email sudah ada
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # buat user baru
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}


# LOGIN
@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):

    # cari user berdasarkan email
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # verifikasi password
    password_valid = verify_password(data.password, user.password)

    if not password_valid:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # generate jwt token
    token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}


# membuat Endpoint profile


# PROFILE
@router.get("/me")
def profile(user=Depends(get_current_user)):

    return {
        "message": "Protected current user success",
        "user": user,
    }
