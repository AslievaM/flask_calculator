import psycopg2
from psycopg2 import sql

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="maryamaslievaicloud.com",
    password="",
    host="localhost"
)

conn.autocommit = True
cur = conn.cursor()

db_name = "calculator"

# Create database
try:
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
    print("Database created")
except:
    print("Database already exists")

cur.close()
conn.close()