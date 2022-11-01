#!/usr/bin/python3
"""A Rectangle model class"""

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor

        Args:
                width (_type_): _description_
                height (_type_): _description_
                x (int, optional): _description_. Defaults to 0.
                y (int, optional): _description_. Defaults to 0.
                id (_type_, optional): _description_. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter func

        Returns:
                int: _description_
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter func for width

        Args:
                value (_type_): assign value to width
        """
        self.__width = value

    @property
    def height(self):
        """height getter func

        Returns:
                int: _description_
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter func for height

        Args:
                value (_type_): assign value to height
        """
        self.__height = value

    @property
    def x(self):
        """x getter func

        Returns:
                int: _description_
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter func for x

        Args:
                value (_type_): assign value to x
        """
        self.__x = value

    @property
    def y(self):
        """y getter func

        Returns:
                int: _description_
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter func for y

        Args:
                value (_type_): assign value to y
        """
        self.__y = value