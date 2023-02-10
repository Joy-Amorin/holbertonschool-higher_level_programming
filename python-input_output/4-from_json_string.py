#!/usr/bin/python3
"""return an objet presented by a JSON
string"""

import json


def from_json_string(my_str):
    """method that returns"""

    return(json.loads(my_str))
