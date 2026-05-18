# FatsApi login Api

Simple authentication Api using FastApi and SQlite.

##  Features

- User Register
- User Login
- JWT Authentication
- Protected Routes
- Password Hashing (bcrypt)
- SQLite Database Integration
- Middleware Logging
- Auto Deploy via GitHub + Railway

---


## technologis
- FastApi
- SQlite 
- pydantic
- jwt 
- paslib
- postgresql

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

```
SWAGGER UI
https://loginsistem-production.up.railway.app/docs
```

# API base URL production 
https://loginsistem-production.up.railway.app

#  Login System API (FastAPI + JWT + SQLite)

Project ini adalah REST API sistem login menggunakan FastAPI, JWT Authentication, dan SQLite sebagai database. Project ini sudah di-deploy menggunakan Railway.

## Tech Stack

- FastAPI
- Python 3.13
- SQLite
- JWT Authentication (JSON Web Token)
- Uvicorn
- Railway Deployment


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

## Authentication Flow
- Register User
- Login User
- Get jwt token
- Access protected routes using
    Authorization: Bearer <token>

## example respone
{
  "message": "FastAPI SQLite Login API running"
}

## Security
- Password hashing menggunakan bcrypt
- JWT token-based Authentication
- Protected route middleware

## Deployment
Project ini di deploy menggunakan:
- Railway cloud platform
- Auto deploy dari Github branch main

#  Database Migration: SQLite → PostgreSQL

Project ini telah diperbarui dari menggunakan SQLite menjadi PostgreSQL untuk mendukung deployment production dan integrasi dengan Railway.

---

##  Perubahan Database

### Sebelumnya — SQLite

Project sebelumnya menggunakan SQLite:

```python
import sqlite3

DATABASE_NAME = "sekolah.db"


## Author
Github : Agung199

