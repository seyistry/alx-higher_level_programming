#!/usr/bin/python3
"""Write a function that writes
   an Object to a text file,
   using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """method to dump json in file

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, 'w', encoding="UTF8") as file:
        json.dump(my_obj, file)
