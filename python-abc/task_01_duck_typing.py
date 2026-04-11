#!/usr/bin/python3
from abc import ABC, abstractmethod
import math
"""second task of abc"""


class Shape(ABC):
    """shape class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """circle class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (abs(self.radius)**2)

    def perimeter(self):
        return math.pi * 2 * abs(self.radius)

class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(shape):
    """duck print with formatted decimals"""

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
