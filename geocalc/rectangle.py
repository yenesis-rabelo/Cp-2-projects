from shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = self._validate_dimension(length)
        self.width = self._validate_dimension(width)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        return f"Rectangle: Length = {self.length:.2f}, Width = {self.width:.2f}, Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

    @staticmethod
    def explain_formulas():
        return "Area = length * width, Perimeter = 2 * (length + width)"

    def _validate_dimension(self, value):
        if value <= 0:
            raise ValueError("Dimensions must be positive.")
        return value
