#!/usr/bin/python3
class Square:
    """Write a class Square that defines a square.
    """
    def __init__(self, size=0):

        """Write a class Square that defines a square by
        private attribuete"""
        self.__size = 3

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
