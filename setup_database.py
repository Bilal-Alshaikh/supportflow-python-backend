import sqlite3

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
""")

cursor.execute("SELECT COUNT(*) FROM customers")
customer_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM payments")
payment_count = cursor.fetchone()[0]

if customer_count == 0 and payment_count == 0:
    cursor.executemany(
        "INSERT INTO customers (id, name) VALUES (?, ?)",
        [(1, "Ahmad"), (2, "Omar")]
    )

    cursor.executemany(
        "INSERT INTO payments (customer_id, amount) VALUES (?, ?)",
        [(1, 400), (1, 250), (2, 700)]
    )

    print("Sample data created successfully.")
else:
    print("Existing data preserved.")

connection.commit()
connection.close()

print("Database setup completed.")