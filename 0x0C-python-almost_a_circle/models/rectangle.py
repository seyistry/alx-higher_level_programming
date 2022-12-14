#!/usr/bin/python3
"""A Rectangle model class"""

from models.base import Base


class Rectangle(Base):
    """A simple Rectangle class"""

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method to calculate area

        Returns:
            int: return the product of height and width
        """
        return self.height * self.width

    def display(self):
        """display area in block
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self) -> str:
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """update method
        """
        for i in range(len(args)):
            if i == 0:
                super().__init__(args[i])
            if i == 1:
                self.width = args[i]
            if i == 2:
                self.height = args[i]
            if i == 3:
                self.x = args[i]
            if i == 4:
                self.y = args[i]

        if len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """method to return class dict rep

        Returns:
            dict: return dict rep
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
