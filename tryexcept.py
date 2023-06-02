def divsion():
    try:
        a=int(input("Enter the number: "))
        assert a>=0, "The value of a cannot be less than 0"
        result =10/a
        print ("result", result)
    except ZeroDivisionError:
       print( "the divisor cannot be zero")
    except ValueError:
        print(" Invalid Input, please enter a valid input")
    else:
        print("No exceptions occured")
    finally:
        print ("exceution complete ")
    

divsion()