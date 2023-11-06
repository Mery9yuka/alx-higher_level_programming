#!/usr/bin/python3
""" Function  that returns the list of attributes and methods of object"""


def lookup(obj):
    """Returns a list of object"""
    return list(dir(obj))
