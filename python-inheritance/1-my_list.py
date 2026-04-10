#!/usr/bin/python3
"""Module that defines a MyList class"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
