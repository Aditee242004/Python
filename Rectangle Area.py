class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display_area(self):
        area = self.length * self.width
        print(f"Area of the Rectangle: {area}")

rect = Rectangle(10, 5)  
rect.display_area()
