def asssertion():
    a=int(input("Enter the first number"))
    assert a>=5, "value of a cannot be less than 5"
    b=int(input("Enter the second number "))
    assert b<=10, "value of b cannot be more than 10"
    s= a+b
    print ("The sum of two number is ",s)

asssertion()