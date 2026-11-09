import sqlite3

def update_payment(cursor, customer, new_amount):
    cursor.execute(
        "UPDATE payments SET amount = ? WHERE customer = ?",
        (new_amount, customer)
    )

connection = sqlite3.connect("supportflow.db")
cursor = connection.cursor()

# 1. Update Ahmad's amount
update_payment(cursor, "Ahmad", 400)

# 2. Save the changes
connection.commit()

# 3. Verify the updated amount
cursor.execute(
    "SELECT amount FROM payments WHERE customer = ?",
    ("Ahmad",)
)

print(cursor.fetchall())

# 4. Close the connection
connection.close()