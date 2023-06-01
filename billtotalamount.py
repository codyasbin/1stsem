class Bill:
    def __init__(self, product, quantity, rate):
        self.product = product
        self.quantity = quantity
        self.rate = rate
    
    def amount(self):
        return self.quantity * self.rate


bills = []  # Create an empty list to store bill objects

while True:
    product = input("Enter the product name (or 'q' to quit): ")
    if product.lower() == 'q':
        break
    quantity = int(input("Enter the quantity: "))
    rate = int(input("Enter the rate: "))

    bill = Bill(product, quantity, rate)
    bills.append(bill)  # Add the bill object to the list

total_amount = sum(bill.amount() for bill in bills)
print("The total amount is:", total_amount)
