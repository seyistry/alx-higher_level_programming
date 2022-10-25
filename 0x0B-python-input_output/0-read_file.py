#!/usr/bin/python3
"""A simple function to reads a text
   file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """a function to read file

    Args:
        filename (str, optional): file name to read.
    """
    with open(filename, encoding="UTF8") as file:
        output = file.read()
        print(output)
