m=int(input("Enter the marks in maths: "))
n=int(input("Enter the marks in nepali: "))
s=int(input("Enter the marks in science: "))
e= int(input('Enter the marks in English: '))
t= m+n+s+e
p=t/4
print("The total marks is :",t)
if p>=80:
    print("your percentage is ",p,"%")
    print("Congratulations! you got distinction")
elif p>=60:
    print("your percentage is ",p,"%")
    print("you got first division")
elif p>=40:
    print("your percentage is ",p,"%")
    print("you got second divison ")
else:
    print("sorry you failed")

def my_function():
    for i in range(30):
        print("Hello world")
my_function()
   
   
