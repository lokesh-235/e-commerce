import sqlite3

def get_db():
    return sqlite3.connect('ecommerce.db')

def create_all_tables():
    from .user import create_user_table
    from .product import create_product_table
    from .order import create_order_table

    create_user_table()
    create_product_table()
    create_order_table()
