class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create objects of Point class
point1 = Point(2, 3)
point2 = Point(4, 5)

# Add two points using the + operator
result = point1 + point2

print(result)  # Output: (6, 8)
