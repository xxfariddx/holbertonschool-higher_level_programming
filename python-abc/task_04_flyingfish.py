#!/usr/bin/python3
"""5th task"""


class Fish:
    """parent 1"""

    def swim(self):
        print("The fish is swimming!")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """parent 2"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    Subclass inheriting from both Fish and Bird.
    The order (Fish, Bird) defines the baseline MRO.
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
