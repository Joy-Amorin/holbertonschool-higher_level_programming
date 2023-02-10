#!/usr/bin/python3
"""createes an objet from a JSON file"""


import json


def load_from_json_file(filename):
    """function to creates an objet"""

    with open(filename) as f:
        j_obj = f.read()
        return(json.loads(j_obj))
