class Teacher:
    def teach(self):
        print("teacher")
        self.name= 'elu pandey'
        self.address='bharatpur'
        self.number= 649624962666

    def printer(self):
        print("name:", self.name)
        print("address:", self.address)
        print("number:", self.number)

tea = Teacher()
tea.teach()
tea.printer()  
