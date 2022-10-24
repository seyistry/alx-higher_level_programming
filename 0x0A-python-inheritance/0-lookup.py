#!/usr/bin/python3
"""A simple function to return attr and methods
"""


def lookup(obj):
    """returns the list of available attributes
        and methods of an object

    Args:
        obj (any): an object or class

    Returns:
        list: returns the list of available
              attributes and methods of an object
    """
    return dir(obj)
