#!/usr/bin/python3
"""third task"""


class VerboseList(list):
    """list class"""

    def remove(self, item):
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """pop function"""

        item = self[index]
        print("Popped {} from the list.".format(item))
        return super().pop(index)

    def append(self, item):
        """append func"""

        print("Added {} to the list.".format(item))
        super().append(item)

    def extend(self, iterable):
        """extend func"""

        x = len(iterable)
        print("Extended the list with {} items.".format(x))
        super().extend(iterable)
