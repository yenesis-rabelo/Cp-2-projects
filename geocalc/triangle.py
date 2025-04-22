from shape import Shape

class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = self._validate_dimension(base)
        self.height = self._validate_dimension(height)
        self.sides = [self._validate_dimension(s) for s in (side_a, side_b, side_c)]

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return sum(self.sides)

    def display_info(self):
        return f"Triangle: Base = {self.base:.2f}, Height = {self.height:.2f}, Sides = {self.sides}, Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

    @staticmethod
    def explain_formulas():
        return "Area = 0.5 * base * height, Perimeter = sum of all sides"

    def _validate_dimension(self, value):
        if value <= 0:
            raise ValueError("All dimensions must be positive.")
        return value
