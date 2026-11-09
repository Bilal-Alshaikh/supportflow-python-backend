import sqlite3
from database import get_customer_total

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()

customer_total = get_customer_total(cursor, 1)
print(customer_total)

connection.close()