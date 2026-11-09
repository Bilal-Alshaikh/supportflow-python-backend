import sqlite3

connection = sqlite3.connect("supportflow_test.db")
cursor = connection.cursor()

def show_payments(cursor):
    cursor.execute("SELECT id, customer, amount FROM payments")
    print(cursor.fetchall())

def add_payment(cursor, customer, amount):
    cursor.execute(
        "INSERT INTO payments (customer, amount) VALUES (?, ?)",
        (customer, amount)
    )

def update_payment_by_id(cursor, id, new_amount):
    cursor.execute(
        "UPDATE payments SET amount = ? WHERE id = ?",
        (new_amount, id)
    )

def delete_payment_by_id(cursor, payment_id):
    cursor.execute(
        "DELETE FROM payments WHERE id = ?",
        (payment_id,)
    )

print(
"=== SupportFlow Menu === \n"
"1. Add Payment \n"
"2. View Payments\n"
"3. Update Payment\n"
"4. Delete Payment\n"
"5. Exit\n")

choice = ""
while choice != "5":
    choice = input("Choose an option 1, 2, 3, 4, or 5: ")
    if choice == "1":
        customer = input("Enter customer name: ")
        amount = input("Enter payment amount: ")
        try:
            amount = int(amount)
            if amount < 0:
                print("Negative payments are not allowed")
            else:
                add_payment(cursor, customer, amount)
                connection.commit()
        except ValueError:
            print("Invalid amount")
    elif choice == "2":
        show_payments(cursor)
    elif choice == "3":
        id = input("Enter customer id number: ")
        new_amount = input("Set a new amount: ")

        try:
            id = int(id)
            new_amount = int(new_amount)
            if new_amount < 0 or id <= 0:
                print("Negative payments are not allowed")
            else:
                update_payment_by_id(cursor, id, new_amount)
                connection.commit()
        except ValueError:
            print("Invalid amount")
    elif choice == "4":
        payment_id = input("Enter customer payment id number: ")
        try:
            payment_id = int(payment_id)
            if payment_id <= 0:
                print("There is no 0 ro negative payment_id")
            else:
                delete_payment_by_id(cursor, payment_id)
                if cursor.rowcount > 0:
                    connection.commit()
                    print("Payment deleted successfully!")
                else:
                    print("Payment ID not found")
        except ValueError:
            print("Invalid payment ID")
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Please choose an option from 1 to 5")
print("Program stopped")

connection.close()