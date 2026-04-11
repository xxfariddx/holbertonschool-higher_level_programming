#!/usr/bin/python3
"""4th task"""


class CountedIterator:
    """class of countediterator"""

    def __init__(self, iteriable):
        self.iterator = iter(iteriable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        return self
