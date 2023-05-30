a=int(input("enter the marks in accont"))
b=int(input("enter the marks in biology"))
c=int(input("enter the marks in chemistry"))
m=int(input("enter the marks in maths"))
p=int(input("enter the marks in physics"))
if a>=35 and b>=35 and c>=35 and m>=35 and p>=35:
    print("pass")
    total=a+b+c+m+p 
    print("total marks is"+str(total))
    gpa=total/25/5
    print("gpa "+str(gpa))
else:
    print("fail") 