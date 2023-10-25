#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """it's a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square.

        Args:
            size (integer): size of the new square.
            position (integer, integer): position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the size of the square."""
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
        """set the position of the square."""
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
        """Return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # in stdout."""
        if self.__size == 0:
            print("")
            return

        [print("") for y in range(0, self.__position[1])]
        for y in range(0, self.__size):
            [print(" ", end="") for u in range(0, self.__position[0])]
            [print("#", end="") for r in range(0, self.__size)]
            print("")
