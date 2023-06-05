class Login:
    @staticmethod
    def log(username, password):
        if username == "asbin" and password == "asbin":
            return True
        else:
            return False

username = input("Enter the username: ")
password = input("Enter the password: ")
lo = Login()
result = lo.log(username, password)

if result:
    print("***LOGIN SUCCESSFUL***")
else:
    print("*****LOGIN UNSUCCESSFUL*****")      
   
         
