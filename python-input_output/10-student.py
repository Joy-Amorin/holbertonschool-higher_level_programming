#!/usr/bin/python3
"""write a class Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """define public attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method  that retrieves a dictionary
         representation of a Student instance """

        output_dict = {}

        if attrs is not None:
            for attr in attrs:
                if hasattr(self, attr):
                    output_dict[attr] = getattr(self, attr)

            return output_dict
        else:
            output_dict = self.__dict__

        return output_dict
