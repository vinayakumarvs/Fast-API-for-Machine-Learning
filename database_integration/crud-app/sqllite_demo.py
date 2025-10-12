import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")

# Print each table name
for table in tables:
    print(table[0])

# Query data from the first table if it exists
if tables:
    first_table = tables[0][0]
    cursor.execute(f"SELECT * FROM {first_table} LIMIT 5;")
    rows = cursor.fetchall()
    print(f"\nFirst 5 rows from table '{first_table}':")
    for row in rows:
        print(row)

# Close the connection
conn.close()

# --- IGNORE ---
# The above code is for demonstration purposes to check the SQLite database content.