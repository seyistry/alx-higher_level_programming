#!/usr/bin/python3
"""A function that returns the dictionary
   description
   with simple data structure
   (list, dictionary, string, integer and boolean)
   for JSON serialization of an object
"""


def class_to_json(obj):
    """covert class to json

    Args:
        obj (_type_): _description_

    Returns:
        object: _description_
    """
    return obj.__dict__
