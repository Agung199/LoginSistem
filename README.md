# FatsApi login Api

Simple authentication Api using FastApi and SQlite.

## Features

- Register User
- login user
- JWt authentication
- Protected route
- SQlite database
- password hashing

## technologis
- FastApi
- SQlite 
- pydantic
- jwt 
- paslib

## instalation 

clone repository:

--bash 
   https://github.com/Agung199/LoginSistem.git

masuk ke folder project:
--bash
    cd app

Buat virtual environment:
```bash
python -m venv venv
```

Activate venv:

### Windows

```bash
venv\\Scripts\\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

install Dependenscy:
```bash
pip install -r requirements.txt
```
## Run Server

```bash
uvicorn main:app --reload
```

## API Documentation

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /register | Register user |
| POST | /login | Login user |
| GET | /me | Protected route 

## Project Structure

```text
app/
 ├── main.py
 ├── database.py
 ├── auth.py
 ├── middleware.py
 ├── schemas.py
 └── routers/

## Author

AGUNG HARY AWAN

