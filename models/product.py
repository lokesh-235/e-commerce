from .db import get_db

def create_product_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER DEFAULT 0,
            description TEXT,
            ImageURL TEXT
        )
    ''')
    conn.commit()
    conn.close()

# SET: Add product
def add_product(name, price, stock, description):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, price, stock, description)
        VALUES (?, ?, ?, ?)
    ''', (name, price, stock, description))
    conn.commit()
    conn.close()

# GET: All products
def get_all_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products
