#!/usr/bin/python3
"""class inherits from list"""


class MyList(list):
    """print list """

    def print_sorted(self):
        print(sorted(self))
