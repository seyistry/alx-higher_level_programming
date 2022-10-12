#!/usr/bin/python3
""" defines a class"""


class Square:
    """ class Square that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ nethod to initialize the size of square
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ setter size nethod to initialize the size of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter size nethod to initialize the size of square
        Args:
            value (tuple): size of square
        Raises:
            TypeError: if `size` is not an integer
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or value[0] < 0 or
                type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """ setter size nethod to initialize the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter size nethod to initialize the size of square
        Args:
            value (int): size of square
        Raises:
            TypeError: if `size` is not an integer
            ValueError: If `size` is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ A class method area that calculate
        the area of a square
        Returns:
            int: return the square of size
        """
        return self.__size * self.__size

    def my_print(self):
        """ print space and #
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(f"{'_' * self.__position[0]}{'#' * self.__size}")
