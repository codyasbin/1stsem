class Nomoneyexceptionn(Exception):
    pass
class outofbudget(Exception):
    pass

balance =int(input("Enter the balance"))
if balance< 500:
    raise Nomoneyexceptionn
elif balance >1000:
    raise outofbudget