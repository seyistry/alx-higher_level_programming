#!/usr/bin/python3
"""
class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """derived class Rectangle

    Args:
        BaseGeometry (_type_): _description_
    """

    def __init__(self, width, height):
        """validates values"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
