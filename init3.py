class student:
    def __init__(self , address, name , number):
        self.address= address
        self.name =name
        self.number =number
    
rose =student("bharatpur","asbin",9824235695)
liyl =student( "chitwan","sandesh",556565)

print(rose.address, rose.name, rose.number)
print(liyl.address, liyl.name, liyl.number)

