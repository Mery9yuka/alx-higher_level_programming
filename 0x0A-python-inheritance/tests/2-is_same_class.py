#!/usr/bin/python3
"""Class that check the function"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.
    Return:
    True if the 'object' is an instance of a class or False otherwise.
    """

    if type(obj) == a_class:
        return True
    else:
        return False