#!/usr/bin/python3
"""function that returns True if the object is exactly
   an instance of the specified class
"""


def inherits_from(obj, a_class):
    """check if obj is a subclass of a_class

    Args:
            obj (_type_): _description_
            a_class (_type_): class

    Returns:
            bool: _description_
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
