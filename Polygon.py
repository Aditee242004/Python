class Polygon:
    def __init__(self, sides):
        self.sides = sides
    
    def display_sides(self):
        print(f"Number of sides: {self.sides}")

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)  # A triangle always has 3 sides
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def display_triangle_info(self):
        self.display_sides()
        print(f"Base: {self.base}")
        print(f"Height: {self.height}")
        print(f"Area of Triangle: {self.calculate_area()}")

if __name__ == "__main__":
    sides = int(input("Enter the number of sides of the polygon: "))
    
    if sides == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        triangle = Triangle(base, height)
        triangle.display_triangle_info()
    else:
        polygon = Polygon(sides)
        polygon.display_sides()
