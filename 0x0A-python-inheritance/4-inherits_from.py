#!/usr/bin/python3
"""class that check objects"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that has been
        inherited from the class.
    Returns:
    True if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class or otherwise False.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
