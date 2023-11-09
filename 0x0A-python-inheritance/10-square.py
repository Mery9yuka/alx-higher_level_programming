#!/usr/bin/python3
"""
    implementinga new square class
"""

Rectangle = __import__("9-rectangle").Rectangle
"""
    a class for rec
"""


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """Instantiation  and width, height"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
