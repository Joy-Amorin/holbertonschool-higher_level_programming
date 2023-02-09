#!/usr/bin/python3
""" returns True if the object is exactly an instance
of the specified class; otherwise False """


def is_same_class(obj, a_class):
    """return fuction"""

    if type(obj) is a_class:

        result = isinstance(obj, a_class)
        return(result)
