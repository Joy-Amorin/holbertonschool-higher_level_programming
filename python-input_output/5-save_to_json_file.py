#!/usr/bin/python3
"""fuction that writes an object to a text file
using JSONrepresentation"""


import json


def save_to_json_file(my_obj, filename):
    """function """

    with open(filename, 'w') as f:
        return (json.dump(my_obj, f))
