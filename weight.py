w=int(input("Enter the weight"))
kgp= input("Kg or pound: ")
if kgp.upper()=='KG':
    wp=w*2.20462
    print ("the weight in pound is", wp)
elif kgp.lower()=="p":
    wkg=w/2.20462
    print("the weight in kg is", wkg)
else:
    print("The value you entered is invalid")





 