#!/usr/bin/python3
"""This module defines a Rectangle class with instance counting,
print_symbol support, and string/representation methods.
"""


class Rectangle:
    """Defines a rectangle with width, height, and instance tracking."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle and increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle as a string using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        line = str(self.print_symbol) * self.__width
        return "\n".join(line for _ in range(self.__height))

    def my_print(self):
        """Print the rectangle using print_symbol."""
        print(self.__str__())

    def __repr__(self):
        """Return a string representation to recreate a new instance."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print message on deletion and decrement counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
