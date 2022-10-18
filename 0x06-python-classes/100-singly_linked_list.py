#!/usr/bin/python3
"""defining a SinglyLinkedList"""


class SinglyLinkedList:
    """ represents a SinglyLinkedList
    Attributes:
        __head (int): size of a side of the square
    """
    def __init__(self):
        """Initializes SinglyLinkedList
        Args:
            __head (any): private head
        Returns: None
        """
        self.__head = []
    
    def sorted_insert(self, value):
        """Initializes SinglyLinkedList
        Args:
            __head (any): private head
        Returns: None
        """
        self.__head.append(value)


    def __str__(self):
        for i in sorted(self.__head):
            print(i)
        try:
            return "thanks"
        except TypeError:
            pass


class Node:
    """ represents a Node
    Attributes:
        ___data (int): size of a side of the square
        ___next_node (tuple): pos of the square
    """
    def __init__(self, data, next_node=None):
        """Initializes Node
        Args:
            __data (int): int type of data
            __next_node (Node): next node in single list
        Returns: None
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter of __data
        Returns:
            return the data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter of __size
        Args:
            value (int): set data value
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter of __next_node
        Returns:
            return the data
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of __next_node
        Args:
            value (int): setter for next_node
        Returns:
            None
        """
        if type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)