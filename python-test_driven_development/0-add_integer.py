#!/usr/bin/python3
"""add two integers """


def add_integer(a, b=98):
    """check if a and b are integers and return the sum """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return(int(a) + int(b))
