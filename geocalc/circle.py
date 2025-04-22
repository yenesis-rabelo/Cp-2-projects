import math
from shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = self._validate_dimension(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        return f"Circle: Radius = {self.radius:.2f}, Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

    @staticmethod
    def explain_formulas():
        return "Area = π * r^2, Perimeter = 2 * π * r"

    def _validate_dimension(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        return value
