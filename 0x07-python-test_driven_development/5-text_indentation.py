#!/usr/bin/python3
"""Module to print square
"""


def text_indentation(text):
    """ A function that prints a text with 2 new lines
        after each of these characters [. ? :]

    Args:
            text (str): text is a type string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (text[i-1] in [".", "?", ":"]) and (text[i] == " "):
            continue
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
