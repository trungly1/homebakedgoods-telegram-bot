import psycopg2

# Database connection parameters - adjust as necessary
db_name = "data"
db_user = "daschronos"
db_password = "Lightspeed123!"
db_host = "localhost"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=db_name, user=db_user, password=db_password, host=db_host
)
conn.autocommit = True
cursor = conn.cursor()

# Database initialization queries
cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(50), chat_id BIGINT);")
# Add more initialization queries as needed

# Close the connection
cursor.close()
conn.close()
