#!/usr/bin/python3
"""Base class"""
import json
from os import path


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""

        if list_dictionaries is None:
            return("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string
        representation of list_objs to a file"""

        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""

        if json_string is None:
            return([])
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all
        attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        if not path.exists(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json", encoding='utf-8') as f:
            list_instance = []
            for dicts in cls.from_json_string(f.read()):
                list_instance.append(cls.create(**dicts))
        return list_instance
