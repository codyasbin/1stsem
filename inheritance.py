class employee:
    def readanddisplay(self):
        self.firstname=input("Enter the first name: ")
        self.lastname = input("Enter the last name: ")
        self.address = input("Enter the address: ")
        self.contact =int(input("Enter the contact: "))
        self.email =input("Enter the email: ")
        self.department =input("Enter the department:")
        print(f"employee name: {self.firstname, {self.lastname}}")
        print(f"address: {self.address}")
        print(f"contact: {self.contact}")
        print(f"email: {self.email}")
        print(f"department: {self.department}")

class FullTimeEmployee(employee):
    def salary(self):
        self.monthly_salary=int(input("Enter the monthly salary: "))
        self.annual_salary =12* self.monthly_salary
        print (f"The monthly salary is :{self.monthly_salary} ")
        print (F"The annual salary is : {self.annual_salary}")

class PartTimeEmployee(employee):
    def salary(self):
        self.hourlypay =int(input('Enter the hourly pay: '))
        self.hoursworked =int(input("Enter the hours worked: "))
        self.salari= self.hourlypay*self.hoursworked
        print(f"Salary of the part time is : {self.salari}")


print("******FULL TIME EMPLOYEE******")
full= FullTimeEmployee()
full.readanddisplay()
full.salary()

print("****PARTTIMEEMPLOYEE*****")
part=PartTimeEmployee()
part.readanddisplay()
part.salary()
