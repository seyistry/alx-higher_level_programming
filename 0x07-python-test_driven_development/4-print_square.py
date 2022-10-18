#!/usr/bin/python3
"""Module to print square
"""


def print_square(size):
    """A function to print size's square

    Args:
        size (int): print "#" * size

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print(f"{'#' * size}")
