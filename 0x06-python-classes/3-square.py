#!/usr/bin/python3
"""defining a class square"""


class Square:
    """Defining a  constructor size of a square"""
    def __init__(self, size=0):
        """initialize a new square

        size is the size of new square we define
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)
