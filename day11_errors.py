import sqlite3
from database import add_payment

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

try:
    add_payment(cursor, 999, 800)
    connection.commit()
except sqlite3.IntegrityError as error:
    connection.rollback()
    print(error)

finally:
    connection.close()