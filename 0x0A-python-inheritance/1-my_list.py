#!/usr/bin/python3
"""class MyList that inherits from
   base class list
"""


class MyList(list):
    """MyList class

    Args:
            list (_type_): Base Class
    """

    def print_sorted(self):
        """print sorted list

        Returns:
                list: return sorted list
        """
        sort_list = sorted(self)
        print(sort_list)
