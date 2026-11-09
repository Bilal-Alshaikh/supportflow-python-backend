import sqlite3
from database import get_payments
from database import get_payment_by_id

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()

payments = get_payments(cursor)
print(payments)
one_payment = get_payment_by_id(cursor, 4)
print(one_payment)

connection.close()