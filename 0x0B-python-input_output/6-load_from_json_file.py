#!/usr/bin/python3
"""A function that creates an
   Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """method to load json from file

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, encoding="UTF8") as file:
        loader = json.load(file)
        return loader
