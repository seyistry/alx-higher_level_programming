#!/usr/bin/python3
""" defines a class"""


class Square:
    """ class Square that defines a square
    """
    def __init__(self, size=0: int):
        """ initialize the size of square

        Args:
            size: size of square

        Raises:
            TypeError: if `size` is not an integer
            ValueError: If `size` is less than 0.

        """
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
