import sqlite3
from constants import DB_NAME

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def close_db_connection(conn):
    conn.close()
