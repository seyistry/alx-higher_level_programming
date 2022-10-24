#!/usr/bin/python3
"""a BaseGeometry module
"""


class BaseGeometry(object):
    """Base Geometry

    Args:
        object (_type_): _description_
    """

    def area(self):
        """area method

        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value > 0 and value int

        Args:
            name (str): _description_
            value (int): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
