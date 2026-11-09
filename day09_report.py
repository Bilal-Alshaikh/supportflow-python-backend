import sqlite3


connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    SELECT customers.name, SUM(payments.amount),  COUNT(*)
    FROM payments
    INNER JOIN customers
    ON payments.customer_id = customers.id
    GROUP BY customers.id, customers.name
    HAVING SUM(amount) > 650
    ORDER BY SUM(payments.amount) DESC
    """
)

print(cursor.fetchall())

connection.close()