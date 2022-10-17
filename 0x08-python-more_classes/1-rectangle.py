#!/usr/bin/python3
""" a module Rectangle
    """


class Rectangle:
    """ class Rectangle that defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        """Instantiate with width and height

        Args:
            width (int, float): value can be an int
                                or float. Defaults to 0.
            height (int, optional): value can be an
                                int or float. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """A getter for function width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """A getter for function height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
