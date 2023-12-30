import sqlite3

# Database file name
DATABASE_FILE = 'my_telegram_bot.db'

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

def create_tables():
    """Create tables in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def initialize_data():
    """Initialize the database with some data."""
    products = [
        ('Blueberry Muffin', 'Muffins', 2.50, 30),
        ('Chocolate Chip Muffin', 'Muffins', 2.75, 25),
        ('Banana Nut Muffin', 'Muffins', 2.50, 20),
        ('Chocolate Chip Cookie', 'Cookies', 1.00, 50),
        ('Oatmeal Raisin Cookie', 'Cookies', 1.00, 40),
    ]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO products (name, category, price, quantity)
        VALUES (?, ?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()

def main():
    """Main function to set up the database."""
    create_tables()
    initialize_data()
    print("Database setup complete with initial data.")

if __name__ == "__main__":
    main()

