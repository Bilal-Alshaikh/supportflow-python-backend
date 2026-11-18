import sqlite3
from services import create_payment

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

tests = [
    (1, -50),
    (0, 500),
    (999, 500)
]

for customer_id, amount in tests:
    try:
        payment_id = create_payment(
            connection, cursor, customer_id, amount
        )
        print("Created:", payment_id)
    except (ValueError, sqlite3.IntegrityError) as error:
        print("Rejected:", error)

connection.close()