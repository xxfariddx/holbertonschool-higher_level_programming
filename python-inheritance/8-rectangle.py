#!/usr/bin/python3
"""Defines Rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
