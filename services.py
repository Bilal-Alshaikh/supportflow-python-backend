from database import add_payment
import sqlite3

def validate_payment(customer_id, amount):
    if type(customer_id) is not int:
        raise ValueError("Invalid customer ID")
    elif type(amount) is not int:
        raise ValueError("Invalid payment amount")
    elif customer_id <= 0:
        raise ValueError("Invalid customer ID")
    elif amount <= 0:
        raise ValueError("Invalid payment amount")
    else:
        return True
    
def create_payment(connection, cursor, customer_id, amount):

    try:
            validate_payment(customer_id, amount)
            payment_id = add_payment(cursor, customer_id, amount)
            connection.commit()
            return payment_id
    except (ValueError, sqlite3.IntegrityError):
        connection.rollback()
        raise