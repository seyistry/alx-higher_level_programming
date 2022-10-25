#!/usr/bin/python3
"""A class Student that defines a student by

    first_name
    last_name
    age

"""

import json


class Student:
    """A simple class student
    """

    def __init__(self, first_name, last_name, age):
        """init object

        Args:
            first_name (str): string
            last_name (str): string
            age (int): integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.first_name, self.last_name)

    def to_json(self):
        """return dict rep of obj

        Returns:
            dict: _description_
        """
        return self.__dict__
