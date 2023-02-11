#!/usr/bin/python3
"""write a class Studen"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """define publics attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that retrieves a dictionary representation of a Student """

        return self.__dict__
