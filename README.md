Login System API (FastAPI + PostgreSQL + JWT)

Simple Authentication REST API menggunakan FastAPI, PostgreSQL, JWT Authentication, dan Role-Based Access Control (RBAC).

Project ini sudah di-deploy menggunakan Railway dan mendukung authentication production-ready.

Features
User Register
User Login
JWT Authentication
Protected Routes
Role-Based Access (Admin/User)
Password Hashing (bcrypt)
PostgreSQL Database
Alembic Database Migration
Middleware Logging
Auto Deploy via GitHub + Railway
Swagger API Documentation


Tech Stack
FastAPI
PostgreSQL
SQLAlchemy
Alembic
JWT (python-jose)
Passlib bcrypt
Pydantic
Uvicorn
Railway


Installation
Clone repository:

git clone https://github.com/Agung199/LoginSistem.git

Masuk ke folder project:

cd LoginSistem

Buat virtual environment:

python -m venv venv

Activate virtual environment:

Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Environment Variables

Buat file .env

DATABASE_PUBLIC_URL=postgresql://username:password@host:port/database
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


Run Server
uvicorn app.main:app --reload


API Documentation

Swagger UI:
http://127.0.0.1:8000/docs

Production Swagger:
https://loginsistem-production.up.railway.app/docs
Production API URL
https://loginsistem-production.up.railway.app


API Endpoints
Method	Endpoint	Description
POST	/register	Register user
POST	/login	Login user
GET	/me	Get current user
GET	/admin	Admin only route


Authentication Flow
Register User
Login User
Get JWT Token
Access protected routes using:
Authorization: Bearer <token>


Project Structure
app/
│
├── main.py
├── database.py
├── middleware.py
├── auth.py
├── dependencies.py
├── schemas/
├── models/
├── routers/
│
├── alembic/
├── alembic.ini
│
├── requirements.txt
└── .env


PostgreSQL Configuration

Project ini menggunakan PostgreSQL dari Railway.

Contoh konfigurasi database:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_PUBLIC_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
Database Migration (Alembic)

Generate migration:

alembic revision --autogenerate -m "create users table"

Apply migration:

alembic upgrade head

Check current migration:

alembic current
Role-Based Access Control (RBAC)

Project ini mendukung role:

user
admin

Contoh endpoint admin:

@app.get("/admin")
def admin_route(current_user = Depends(get_current_admin)):
    return {"message": "Welcome Admin"}


Security
Password hashing menggunakan bcrypt
JWT token authentication
Protected routes
Role-based authorization
Environment variables (.env)

Deployment
Project ini di-deploy menggunakan:

Railway
GitHub Auto Deploy
PostgreSQL Railway Database
Example Response
{
  "message": "FastAPI PostgreSQL Login API running"
}


Future Improvements
Email Verification
Refresh Token
Docker Support
CI/CD Pipeline
Redis Caching
Unit Testing
Rate Limiting

Author
GitHub:

Agung199/LoginSistem