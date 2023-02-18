#!/usr/bin/python3
"""write square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):

        _str = (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
        return(_str)

    @property
    def size(self):
        """size getter"""
        return(self.width)

    @size.setter
    def size(self, value):
        """size setter"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes to list args"""

        if len(args) > 0:
            arg_list = ["id", "size", "x", "y"]

            for i, arg in zip(arg_list, args):
                setattr(self, i, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        dict_square = {"id": self.id, "size": self.size,
                       "x": self.x, "y": self.y}
        return(dict_square)
