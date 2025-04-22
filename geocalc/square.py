from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def display_info(self):
        return f"Square: Side = {self.length:.2f}, Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

    @staticmethod
    def explain_formulas():
        return "Area = side^2, Perimeter = 4 * side"
