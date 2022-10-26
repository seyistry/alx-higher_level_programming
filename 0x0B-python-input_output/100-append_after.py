#!/usr/bin/python3
"""A function that inserts a line of text to a file,
   after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Append after search string

    Args:
        filename (str, optional): _description_. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode="r", encoding="UTF8") as fp:
        content = fp.readlines()
    with open(filename, mode="w", encoding="UTF8") as fp:
        for row in content:
            fp.write(row)
            if row.find(search_string) != -1:
                fp.write(new_string)
