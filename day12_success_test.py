import sqlite3
from services import create_payment
from database import get_payment_by_id

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

payment_id = create_payment(connection, cursor, 1, 350)
value = get_payment_by_id(cursor, payment_id)
print(value)

connection.close()