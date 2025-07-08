from .db import get_db
from datetime import datetime

def create_order_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER DEFAULT 1,
            order_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    ''')
    conn.commit()
    conn.close()

# SET: Place an order
def create_order(user_id, product_id, quantity):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (user_id, product_id, quantity, order_date)
        VALUES (?, ?, ?, ?)
    ''', (user_id, product_id, quantity, datetime.now()))
    conn.commit()
    conn.close()

# GET: All orders for a user
def get_orders_by_user(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT orders.id, products.name, orders.quantity, orders.order_date
        FROM orders
        JOIN products ON orders.product_id = products.id
        WHERE orders.user_id = ?
    ''', (user_id,))
    orders = cursor.fetchall()
    conn.close()
    return orders
