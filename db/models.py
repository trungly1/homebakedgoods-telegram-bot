CREATE_TABLE_PRODUCTS = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    image_url TEXT
);
"""

def create_tables(conn):
    try:
        conn.execute(CREATE_TABLE_PRODUCTS)
    except Exception as e:
        print(f"An error occurred: {e}")
