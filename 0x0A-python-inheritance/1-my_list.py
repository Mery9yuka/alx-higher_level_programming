#!/usr/bin/python3
""" a class Module
"""


class MyList(list):
    """a class inherited from list that print the list in sorted order."""

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order and 
        it does not modify it
        """
        print(sorted(self))
