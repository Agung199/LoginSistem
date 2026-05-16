# MEMBUAT ROUTER AUTHENTICATION
from fastapi import APIRouter
from fastapi import HTTPException, Depends

from app.database import get_connection

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


@router.post("/register")
def register(data: RegisterSchema):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (data.email,))

        existing_user = cursor.fetchone()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already exists")

        hashed_password = hash_password(data.password)

        cursor.execute(
            """
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
            """,
            (data.username, data.email, hashed_password),
        )

        conn.commit()

        return {"message": "User created successfully"}

    finally:
        conn.close()


@router.post("/login")
def login(data: LoginSchema):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (data.email,))

    user = cursor.fetchone()

    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    password_valid = verify_password(data.password, user["password"])

    if not password_valid:
        raise HTTPException(status_code=401, detail="invalid email or password")

    token = create_access_token(data={"sub": str(user["id"])})

    return {"access_token": token, "toekn_type": "bearer"}


# membuat Endpoint profile


@router.get("/me")
def profile(user=Depends(get_current_user)):

    return {"message": "Protected current user success", "user": user}
