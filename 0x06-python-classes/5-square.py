#!/usr/bin/python3
"""defining a class square"""


class Square:
    """Defining a  constructor size of a square"""
    def __init__(self, size=0):
        """initialize new square

        size, is the size of new square we defined
        """
        self.__size = size

    @property
    def size(self):
        """set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print a square with # in stdout"""
        for y in range(0, self.__size):
            [print("#", end="") for u in range(self.__size)]
            print("")
        if self.size == 0:
            print("")
