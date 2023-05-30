y=int(input("enter the year: "))
if y%400==0 and y%4==0 or y%100!=0:
    print("The year is leap year")
else:
    print("The year is not leap year")