from .db import get_db

def create_user_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def get_user_by_username(username):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# SET method – Create user
def create_user(username, email, password):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
    ''', (username, email, password))
    conn.commit()
    conn.close()

# GET method – Fetch user by username and password
def get_user_by_credentials(username, password):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username=? AND password=?
    ''', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user
