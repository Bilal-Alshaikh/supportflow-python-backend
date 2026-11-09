import sqlite3

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
try:
    cursor.execute("SELECT * FROM invoices")
    print(cursor.fetchall())

except sqlite3.OperationalError as error:
    print("Database operation failed:", error)

finally:
    connection.close()

print("Program finished")