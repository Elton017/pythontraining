import math

class Shape:
    def __init__(self, name):
        self.name = name
        
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
            
    def area(self):
        return self.radius ** 2 * math.pi

rectangle = Rectangle("Rectangle", 4, 5)
circle = Circle("Circle", 3)

print(f"{rectangle.name} Area:", rectangle.area())
print(f"{circle.name} Area:", circle.area()) 