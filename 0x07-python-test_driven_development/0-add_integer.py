#!/usr/bin/python3
""" 0-add_integer is a module
    that add two integer together

    with add_integer as the only function
    """


def add_integer(a, b=98):
    """ A function to Add two integers

    Args:
        a (int, float): a value must be int or float
        b (int, float): b value must be int or float. Defaults to 98.

    Raises:
        TypeError: if a and b is not an Int or float

    Returns:
        int: return a int
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
