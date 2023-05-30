cu=int(input("enter the current unit"))
pu=int(input("enter the previous unit"))
tu=cu-pu
print("total unit is"+str(tu))
if tu>200:
    ta=(tu-200)*10+(200-20)*8+100
    print("Total amount is "+str(ta))
elif tu<200:
    ta=(tu-20)*8+100
    print("total amount is "+str(ta))
else:
    ta=100
    print("total amount is"+str(ta))
      