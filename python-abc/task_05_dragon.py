#!/usr/bin/python3
"""6th task"""


class SwimMixin:
    """SwimMixin class"""

    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """FlyMixin class"""

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """class of Dragon"""

    def roar(self):
        print("The dragon roars!")
