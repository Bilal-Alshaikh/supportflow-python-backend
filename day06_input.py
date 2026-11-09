customer = input("Enter your name: ")
amount = input("Enter payment amount: ")

try:
    amount = int(amount)
    if amount < 0:
        print("Negative payments are not allowed")
    else:
        print("Customer: " + customer)
        print("Amount: " + str(amount))
        print(type(amount))
except ValueError:
    print("Invalid payment amount")