def get_payments(cursor):
    cursor.execute("SELECT id,customer_id, amount FROM payments")
    return cursor.fetchall()

def add_payment(cursor, customer_id, amount):
    cursor.execute(
        "INSERT INTO payments (customer_id, amount) VALUES (?, ?)",
        (customer_id, amount))
    return cursor.lastrowid

def get_payment_by_id(cursor, payment_id):
    cursor.execute("SELECT id,customer_id, amount FROM payments WHERE id = (?)",
    (payment_id,))
    return cursor.fetchone()

def get_customer_total(cursor, customer_id):
    cursor.execute("""
    SELECT SUM(amount)
    FROM payments
    WHERE customer_id = (?)
    """,
    (customer_id,))
    return cursor.fetchone()