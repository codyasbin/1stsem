class Bill:
    def __init__(self, product, quantity, rate):
        self.product = product
        self.quantity = quantity
        self.rate = rate
    
    def amount(self):
        return self.quantity * self.rate
    
    @staticmethod
    def total_amount(bills):
        total = 0
        for bill in bills:
            total += bill.amount()
        return total

bills = []  # Create an empty list to store bill objects

product = input("Enter the product name: ")
quantity = int(input("Enter the quantity: "))
rate = int(input("Enter the rate: "))

bill = Bill(product, quantity, rate)
bills.append(bill)  # Add the bill object to the list

print("The amount is:", bill.amount())
print("The total amount is:", Bill.total_amount(bills))




