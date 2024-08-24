import sqlite3
import pandas as pd

# Step 1: Create a SQLite database and insert data
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

conn.commit()
conn.close()

# Step 2: Import data into a DataFrame
conn = sqlite3.connect('example.db')
df = pd.read_sql_query("SELECT * FROM users", conn)
conn.close()

print(df)

def insert_sql(name, age):
    