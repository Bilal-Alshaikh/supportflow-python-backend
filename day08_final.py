import sqlite3

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    SELECT customers.name, SUM(payments.amount)
    FROM payments
    INNER JOIN customers
    ON customers.id = payments.customer_id
    GROUP BY customers.id, customers.name""")
print(cursor.fetchall())

connection.close()