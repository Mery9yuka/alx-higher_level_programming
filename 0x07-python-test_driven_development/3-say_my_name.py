#!/usr/bin/python3
"""Defineing a function that prints name."""


def say_my_name(first_name, last_name=""):
    """function that Prints a name.
    Raises:
        TypeError: If the first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
