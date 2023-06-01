class Calculator:
    def __init__(self, first_number , second_number):
        self.first_number =first_number
        self.second_number =second_number
    def addition(self):
        return self.first_number+self.second_number
    def multiplication(self):
        return self.first_number*self.second_number
    def division(self):
        return self.first_number/self.second_number
while True:
    calculation=input("Do you want to calculate? presse to exit")
    if calculation.lower() =='e':
        break
    first_number=int(input("Enter the first number: "))
    second_number=int(input("Enter the second number: "))
    cal=Calculator(first_number, second_number)

print("The addition of the numbers is : ", cal.addition())
print("The multiplicatio  of the number is :", cal.multiplication())
print("The division of the number is :", cal.division())
