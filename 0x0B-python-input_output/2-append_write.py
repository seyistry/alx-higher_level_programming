#!/usr/bin/python3
"""A simple function that appends a string to a text file
   (UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): file name to write to.
        text (str, optional): text to write into file
    """
    with open(filename, mode="a", encoding="UTF8") as file:
        return file.write(text)
