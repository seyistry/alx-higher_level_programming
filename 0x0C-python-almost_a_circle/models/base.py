#!/usr/bin/python3
"""A Base class for this module"""


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
