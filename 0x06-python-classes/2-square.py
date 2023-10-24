#!/usr/bin/python3
"""defining a class square"""


class Square:
    """Define instance of the Square class with given size"""
    def __init__(self, size=0):
        """define a new square

        size, is the size of the new square we defined
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
