import math

class Shapes:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    
    # Here i tells us that area and circumference methods only works if there are subclasses
    @property 
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    @property
    def circumference(self):
        raise NotImplementedError("Subclasses must implement this method")

    
    # returns an object in string format
    def __repr__(self):
        return f"{type(self).__name__(x={self.x}, y={self.y})}"

    def __str__(self):
        return f"{type(self).__name__(x={self.x}, y={self.y})}"

    
    # translates the shapes
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_inside(self, x, y):
        raise NotImplementedError("subclasses must implement this method")


class Rectangle(Shapes):
    def __init__(self, x, y, side1, side2):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def circumference(self):
        return 2 * (self.side1 + self.side2)
    
    
    # Checking if rectangle is a square
    def is_square(self):
        return self.side1 == self.side2
    

    # checks if a given point is inside the rectangle
    def is_inside(self, x, y):
        try:
            return (
                self.x <= x <= self.x + self.side1 and
                self.y <= y <= self.y + self.side2
            )
        except Exception as e:
            print(f"Error in Rectangle.is_inside: {e}")
            return False
        
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (
                self.x == other.x
                and self.y == other.y
                and self.side1 == other.side1
                and self.side2 == other.side2
            )
        return False
            
class Circle(Shapes):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def if_unit_circle(self):
        return self.radius == 1
    
    def is_inside(self, x, y):
        distance_squared = (x - self.x) ** 2 + (y + self.y) ** 2
        return distance_squared <= self.radius ** 2
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.x == other.x and self.y == other.y and self.radius == other.radius
        return False
            

circle1 = Circle(x=0,y=0, radius=1) # enhetscirkel 
circle2 = Circle(x=1,y=1, radius=1)
rectangle = Rectangle(x=0,y=0,side1=1, side2=1)

print(circle1==circle2) # True
print(circle2==rectangle) # False
print(circle1.is_inside(0.5, 0.5)) # True
circle1.translate(5,5)
print(circle1.is_inside(0.5, 0.5)) # False
try:
    circle1.translate("THREE",5) 
except ValueError as e:
    print(f"Error {e}")
