#!/usr/bin/python3
""" defines a class"""


class Square:
    """ class Square that defines a square
    """
    def __init__(self, size=0):
        """ __init__ nethod to initialize the size of square
        """
        self.__size = size

    def size(self):
        """ setter size nethod to initialize the size of square
        """
        return self.__size

    def size(self, value):
        """ setter size nethod to initialize the size of square

        Args:
            value (int): size of square

        Raises:
            TypeError: if `size` is not an integer
            ValueError: If `size` is less than 0.

        """
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ A class method area that calculate
        the area of a square

        Returns:
            int: return the square of size
        """
        return self.__size * self.__size
