from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

    @staticmethod
    @abstractmethod
    def explain_formulas():
        pass

    def has_larger_area(self, other):
        return self.area() > other.area()

    def has_longer_perimeter(self, other):
        return self.perimeter() > other.perimeter()
