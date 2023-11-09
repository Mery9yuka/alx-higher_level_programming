#!/usr/bin/python3
"""Class that check the function"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specific class or not
    Return:
    True if the object is an instance of a class or False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
