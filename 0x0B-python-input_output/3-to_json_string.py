#!/usr/bin/python3
"""Write a function that returns the
   JSON representation of an object (string):
"""

import json


def to_json_string(my_obj):
    """covert obj to json

    Args:
        my_obj (object): object to json

    Returns:
        object: JSON object
    """
    return json.dumps(my_obj)
