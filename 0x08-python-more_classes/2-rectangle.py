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
        """func to set width

        Args:
            value (int): value for width

        Raises:
            TypeError: if type not int
            ValueError: if value is less than 0
        """
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
        """func to set height

        Args:
            value (int): value for height

        Raises:
            TypeError: if type not int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """A function to calculate area of rectangle

        Returns:
            int: An Area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """A function to calculate the parameter

        Returns:
            int: the parameter of rectangle
        """
        if area() == 0:
            return 0
        return 2 * (self.width + self.height)
