import sqlite3

DATABASE_NAME = "sekolah.db"


# CONNECT DATABASE
def get_connection():
    conn = sqlite3.connect("sekolah.db")
    conn.row_factory = sqlite3.Row

    return conn


# MEMBUAT TABLE USER
def create_user_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
