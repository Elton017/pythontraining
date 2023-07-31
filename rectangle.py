class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter
    
    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

rec1 = Rectangle(100,1000)

print(rec1.is_square())
print(rec1.get_perimeter())
print(rec1.get_area())