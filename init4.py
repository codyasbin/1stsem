class maths:
    def __init__(self, length, breadth, height):
        self.length=length
        self.breadth= breadth
        self.height= height

    def calculate_area(self):
        return self.length*self.breadth
    def calculate_perimeter(self):
        return 2*(self.length + self.breadth)
    def calculate_volume(self):
        return self.length* self.breadth*self.height
    
length=int(input("Enter the length: "))
breadth =int(input("Enter the breadth: "))
height =int(input("Enter the height: "))

Maths=maths(length, breadth, height)
area=Maths.calculate_area()
perimeter= Maths.calculate_perimeter()
volume =Maths.calculate_volume()

print("area is: ", area)
print("volume is: ", volume)
print("perimeter is: ", perimeter)
