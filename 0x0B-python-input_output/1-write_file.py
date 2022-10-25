#!/usr/bin/python3
"""A simple function that writes a string to a text file
   (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): file name to write to.
        text (str, optional): text to write into file
    """
    with open(filename, mode="w", encoding="UTF8") as file:
        return file.write(text)
