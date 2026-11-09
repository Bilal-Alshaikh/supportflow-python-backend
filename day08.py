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

cursor.execute(
    "INSERT INTO customers (name) VALUES (?)",
    ("Ahmad",)
)
connection.commit()

cursor.execute(
    "INSERT INTO customers (name) VALUES (?)",
    ("Omar",)
)
connection.commit()

cursor.execute(
    "INSERT INTO payments (customer_id, amount) VALUES (?, ?)",
    (1, 400)
)
connection.commit()

cursor.execute(
    "INSERT INTO payments (customer_id, amount) VALUES (?, ?)",
    (1, 250)
)
connection.commit()

cursor.execute(
    "INSERT INTO payments (customer_id, amount) VALUES (?, ?)",
    (2, 700)
)
connection.commit()

cursor.execute("""
    SELECT customers.name, payments.amount
    FROM payments
    INNER JOIN customers
    ON payments.customer_id = customers.id
    """
)
print(cursor.fetchall())
connection.close()