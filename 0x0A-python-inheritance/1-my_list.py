#!/usr/bin/python3
"""class MyList that inherits from
   base class list
"""


class MyList(list):
    """MyList class

    Args:
            list (_type_): Base Class
    """

    def __init__(self):
        """"initializes the object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list

        Returns:
                list: return sorted list
        """
        sort_list = sorted(self)
        print(sort_list)
