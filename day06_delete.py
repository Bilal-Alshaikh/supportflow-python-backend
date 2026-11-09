import sqlite3

# 1. Connect to the TEST database
connection = sqlite3.connect("supportflow_test.db")
cursor = connection.cursor()

# 2. Ask the user for the payment ID
payment_id = input("Enter payment ID to delete: ")

# 3. Validate and delete the payment
try:
    payment_id = int(payment_id)

    if payment_id <= 0:
        print("Payment ID must be positive")

    else:
        cursor.execute(
            "DELETE FROM payments WHERE id = ?",
            (payment_id,)
        )

        # Check whether a payment was actually deleted
        if cursor.rowcount > 0:
            connection.commit()
            print("Payment deleted successfully!")
        else:
            print("Payment ID not found")

except ValueError:
    print("Invalid payment ID")

# 4. Show remaining payments
cursor.execute(
    "SELECT id, customer, amount FROM payments"
)

print("Remaining payments:")
print(cursor.fetchall())

# 5. Close the database connection
connection.close()