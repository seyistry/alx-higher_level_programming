#!/usr/bin/python3
"""A class MyInt that inherits from int
"""


class MyInt(int):
    """Class Myint

    Args:
        int (_type_): _description_
    """

    def __eq__(self, other):
        """magic method eqauall to

        Args:
            other (_type_): _description_

        Returns:
            bool: _description_
        """
        return self.__int__ == other

    def __ne__(self, other):
        """magic method not equall to

        Args:
            other (_type_): _description_

        Returns:
            bool: _description_
        """
        return self.__int__ != other
