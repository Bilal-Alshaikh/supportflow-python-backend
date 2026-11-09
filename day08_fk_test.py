import sqlite3

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
try:
    cursor.execute(
    "INSERT INTO payments (customer_id, amount) VALUES (?, ?)",
    (999, 500)
    )
    connection.commit()
except sqlite3.IntegrityError as error:
    print("Database rejected the payment:", error)

connection.close()