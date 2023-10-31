#!/usr/bin/python3
"""Defining a locked class."""


class LockedClass:
    """
    Prevent the user from dynamically creating new instance attributes
    except if it   called 'first_name'
    """
    __slots__ = ["first_name"]
