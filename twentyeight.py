a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a>c:
    print("the greatest number is"+str(a))
elif b>a and b>c:
    print("the greatest number is"+str(b))
else:
    print("the greatest number is"+str(c))
    