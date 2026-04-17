#!/usr/bin/python3
"""
Module that defines a Student class with selective JSON output
"""


class Student:
    """Defines a student by name and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        """
        # 1. Check if attrs is a list of strings
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res

        # 2. If attrs is not a list of strings, return everything
        return self.__dict__
