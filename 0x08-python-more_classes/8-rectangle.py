#!/usr/bin/python3
""" a module Rectangle
    """


class Rectangle:
    """ class Rectangle that defines a Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if 0 in [self.height, self.width]:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """func docstring

        Returns:
            str: docstring
        """
        rec_diagram = ""
        if not (0 in [self.height, self.width]):
            for i in range(self.height):
                if i == (self.height - 1):
                    rec_diagram += (str(self.print_symbol) * self.width)
                else:
                    rec_diagram += (str(self.print_symbol) * self.width) + "\n"
        return rec_diagram

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to check which rect is bigger

        Args:
            rect_1 (Rectangle): an instance of class Rectangle
            rect_2 (Rectangle): an instance of class Rectangle

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle

        Returns:
            Rectangle: an instance of class Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return rect_2 if rect_2.area() > rect_1.area() else rect_1
