a=int(input("Enter a number: "))
b=sum(int(digit)**len(str(a))for digit in str(a))
if b==a:
    print("The number is armstrong")
else:
    print("The numberis not a armstrong")
