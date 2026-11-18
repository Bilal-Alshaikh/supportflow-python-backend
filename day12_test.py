from services import validate_payment

tests = [
    (1, 500),
    (0, 500),
    (1, -50),
    ("Ahmad", 500),
    (1, "500"),
    (True, 500)
]

for customer_id, amount in tests:
    try:
        result = validate_payment(customer_id, amount)
        print("Valid:", result)
    except ValueError as error:
        print("Rejected:", error)