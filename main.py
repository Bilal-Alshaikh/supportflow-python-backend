import sqlite3


def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY,
            customer TEXT,
            amount INTEGER
        )
    """)


def add_payment(cursor, customer, amount):
    cursor.execute(
        "INSERT INTO payments (customer, amount) VALUES (?, ?)",
        (customer, amount)
    )


def get_payments(cursor):
    cursor.execute("SELECT customer, amount FROM payments")
    result = cursor.fetchall()
    return result


connection = sqlite3.connect("supportflow.db")
cursor = connection.cursor()

create_table(cursor)
customer = input("Enter your name: ")
amount = input("Enter payment amount: ")

try:
    amount = int(amount)
    if amount < 0:
        print("Negative payments are not allowed")
    else:
        print("Customer: " + customer)
        print("Amount: " + str(amount))
        add_payment(cursor, customer, amount)
        connection.commit()

except ValueError:
    print("Invalid payment amount")

print(get_payments(cursor))
connection.close()