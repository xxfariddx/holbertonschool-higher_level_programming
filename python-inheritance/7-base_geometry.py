#!/usr/bin/python3
"""
Module defining the BaseGeometry class.
"""


class BaseGeometry:
    """A class with geometric functions and validation."""

    def area(self):
        """Raises an Exception as it's not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
