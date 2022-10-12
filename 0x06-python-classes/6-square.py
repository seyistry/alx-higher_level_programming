#!/usr/bin/python3
"""defining a square"""


class Square:
    """ represents a square
    Attributes:
        ___size (int): size of a side of the square
        ___position (tuple): pos of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square
        Args:
            size (int): size of a side of the square
            position (tuple): pos of the square
        Returns: None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates square's area
        Returns: None
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The square's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the square's size
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Prints square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")

    @property
    def position(self):
        """getter of __position
        Returns:
            position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
