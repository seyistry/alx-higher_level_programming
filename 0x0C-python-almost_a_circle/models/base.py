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

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert dict to json

        Args:
            list_dictionaries (dict): _description_

        Returns:
            dict: json dumps
        """
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file

        Args:
            list_objs (_type_): _description_
        """
        file = []
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                file.append(cls.to_dictionary(i))
        with open(file_name, "w") as fp:
            fp.write(cls.to_json_string(file))
