#!/usr/bin/python3
"""A Base class for this module"""

import json


class Base:
    """Base Class
       with private attr __nb_object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ base constructor

        Args:
            id (int, None): can be a None or a +int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """convert dict to json

        Args:
            list_dictionaries (dict): _description_

        Returns:
            dict: json dumps
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
