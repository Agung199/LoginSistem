from jose import jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


def create_access_token(user):
    data = {"sub": user.email, "role": user.role}

    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
