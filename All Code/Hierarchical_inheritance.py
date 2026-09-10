class Shape:
    def area(self): return 0

class Circle(Shape):
    def area(self): 
        return 3.14 * self.r ** 2

class Rectangle(Shape):
    def area(self): 
        return self.w * self.h

class Triangle(Shape):
    def area(self):
        return 0.5 * self.b * self.h

a=Shape()

print(a.area())
print(a.area())
print(a.area())