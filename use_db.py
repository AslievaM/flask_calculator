import psycopg2

# 🔹 CONNECT to your new database
conn = psycopg2.connect(
    dbname="calculator",
    user="maryamaslievaicloud.com",
    password="",
    host="localhost"
)

cur = conn.cursor()

# 🔹 CREATE TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS history (
    id SERIAL PRIMARY KEY,
    operation TEXT,
    result TEXT
)
""")

conn.commit()

# 🔹 INSERT DATA
cur.execute(
    "INSERT INTO history (operation, result) VALUES (%s, %s)",
    ("2 + 2", "4")
)

conn.commit()

# 🔹 READ DATA
cur.execute("SELECT * FROM history")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()