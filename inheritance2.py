class RoundedObject:
    def getAndSetvalues(self):
        self.radius=int(input("Enter the radius: "))
        self.height=int(input("Enter the height: "))
import math
class circle(RoundedObject):
    def area(self):
        return  math.pi*self.radius**2
    def circumference(self):
        return 2*math.pi*self.radius
class cylinder(RoundedObject):
    def curvedSurfaceArea(self):
        return 2*math.pi*self.radius*self.height
    def totalSurfaceArea(self):
        return 2*math.pi*self.radius*(self.radius+self.height)
    def volume(self):
        return math.pi*math.pow(self.radius,2)*self.height
cir= circle()
cir.getAndSetvalues()
print(f"The area of the circle is : {cir.area()}")
print(f"The circumference of the circle is : {cir.circumference()}")
cyl=cylinder()
cyl.getAndSetvalues()
print(f"The curvedsurface area of the cylinder is: {cyl.curvedSurfaceArea()}")
print(f"The total surface area of the cylinder is: {cyl.totalSurfaceArea()}")
print(f"The volume of the cylinder is: {cyl.volume()}")
        