#!/usr/bin/python3
"""function that returns True if the object is exactly
   an instance of the specified class
"""


def is_kind_of_class(obj, a_class):
    """check if obj is a class a_class

    Args:
            obj (_type_): _description_
            a_class (_type_): class

    Returns:
            bool: _description_
    """
    return isinstance(obj, a_class)
