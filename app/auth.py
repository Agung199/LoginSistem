# MEMBUAT AUNTHENTICATION HELPER

from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# membuat protected route
from fastapi import Depends
from fastapi import HTTPException
from app.models import user_model
#from app.security.jwt import get_current_user

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
import hashlib

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    # bypass limit 72 bytes bcrypt
    password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    plain_password = hashlib.sha256(plain_password.encode("utf-8")).hexdigest()

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return payload

    except JWTError:
        return None


# membuat protected route
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials

    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="invalid token")

    return payload


def require_admin(current_user: user_model = Depends(get_current_user)):

    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return current_user
