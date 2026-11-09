import sqlite3
from database import get_customer_total

connection = sqlite3.connect("supportflow_day08.db")
cursor = connection.cursor()

print("Omar total:", get_customer_total(cursor, 2))

connection.close()