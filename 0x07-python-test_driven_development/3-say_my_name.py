#!/usr/bin/python3
""" 3-say_my_name is a module
    that print first name and last name

    with say_my_name as the only function
    """


def say_my_name(first_name, last_name=""):
    """ a function that prints My name is <first name> <last name>

    Args:
            first_name (str): a string value for first name.
            last_name (str): a string of last name.
    """
    # print(f"first Name: {first_name} type is: {type(first_name)}")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        if first_name.isnumeric():
            raise TypeError("first_name must be a string")
        if last_name.isnumeric():
            raise TypeError("last_name must be a string")
        print(f"My name is {first_name} {last_name}")
