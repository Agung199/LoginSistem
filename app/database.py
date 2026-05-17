# import sqlite3

# DATABASE_NAME = "sekolah.db"


# CONNECT DATABASE
# def get_connection():
# onn = sqlite3.connect("sekolah.db", timeout=10, check_same_thread=False)
# conn.row_factory = sqlite3.Row

# return conn

from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
import os


load_dotenv()


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:KLtNHJrxaitSDZvMlzyLyGHgczCIseEF@postgres.railway.internal:5432/railway",
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# MEMBUAT TABLE USER
# def create_user_table():
# conn = get_connection()
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# username TEXT NOT NULL,
# email TEXT UNIQUE NOT NULL,
# password TEXT NOT NULL,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# """)

# conn.commit()
# conn.close()
