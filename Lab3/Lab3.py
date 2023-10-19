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
        try:
            self.x += float(dx)
            self.y += float(dy)
        except ValueError as e:
            raise ValueError(f"Translation error: {e}")

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
        return (
            self.x - self.side1 / 2 <= x <= self.x + self.side1 / 2 and
            self.y - self.side2 / 2 <= y <= self.y + self.side2 / 2
        )
    
    # Comparing equality
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (
                super().__eq__(other) and
                self.side1 == other.side1 and
                self.side2 == other.side2
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
        distance_squared = (x - self.x) ** 2 + (y - self.y) ** 2
        return distance_squared <= self.radius ** 2
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return (
                 self.x == other.x 
                 and self.y == other.y 
                 and self.radius == other.radius
            )
        return False
    
    def is_square(self):
        return False
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return (
                super().__eq__(other) and 
                self.radius == other.radius
            )
        return False
    
class Cube(Shapes):
    def __init__(self, x, y, z, side_length):
        super().__init__(x, y)
        self.side_length = side_length
        self.z = z

    def volume(self):
        return self.side_length ** 3
    
    
    def circumference(self):
        raise NotImplementedError("circumference does not exist for cube")
    
    def is_inside(self, x, y, z):
        return (
            self.x - self.side_length / 2 <= x <= self.x + self.side_length / 2 and
            self.y - self.side_length / 2 <= y <= self.y + self.side_length / 2 and
            self.z - self.side_length / 2 <= z <= self.z + self.side_length / 2
        )
    
    def __eq__(self, other):
        return (
            super().__eq__(other) and 
            self.z == other.z and
            self.side_length == other.side_length
        )

    

class Sphere(Shapes):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y)
        self.z = z
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2
    
    def circumference(self):
        raise NotImplementedError("circumference does not exist for cube")
    
    def is_inside(self, x, y, z):
        distance_squared = (x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2
        return distance_squared <= self.radius ** 2
                  
    def __eq__(self, other):
        return (
            super().__eq__(other) and 
            self.z == other.z and
            self.radius == other.radius
        )
    
    @property 
    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    
if __name__ == "__main__":
    circle1 = Circle(x=0,y=0, radius=1) # enhetscirkel 
    circle2 = Circle(x=1,y=1, radius=1)
    rectangle = Rectangle(x=0,y=0,side1=1, side2=1)

    print(circle1 == circle2)  # True
    print(circle2 == rectangle)  # False
    print(circle1.is_inside(0.5, 0.5))

    try:
        circle1.translate(5, 5)
    except ValueError as e:
        print(f"ValueError: {e}")

    print(circle1.is_inside(0.5, 0.5))

    try:
        circle1.translate("THREE", 5)  # Should raise ValueError
    except ValueError as e:
        print(f"ValueError: {e}")










