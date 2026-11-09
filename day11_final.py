import sqlite3
from database import add_payment

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

try:
    add_payment(cursor, 2, 300)
    add_payment(cursor, 999, 400)
    connection.commit()

except sqlite3.IntegrityError:
    connection.rollback()
    print("Batch rejected")

except sqlite3.OperationalError:
    connection.rollback()
    print("Database operation failed")

finally:
    connection.close()