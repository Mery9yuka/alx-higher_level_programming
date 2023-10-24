#!/usr/bin/python3
"""defining a class square"""


class Square:
    """Defining a  constructor size of a square"""
    def __init__(self, size=0):
        """initialize new square

        size, is the size of new square we defined
        """
        self.__size = size
        self.__position = (0, 0)

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

    @property
    def position(self):
        """set the position of square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return
        for y in range(self.__position[1]):
            print("")
        for y in range(self.__size):
            for u in range(self.__position[0]):
                print(" ", end="")
            for u in range(self.__size):
                print("#", end="")
            print("")
