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
        
    def __str__(self):
        """return  rectangle description: [Square] <size>/<size>"""
        stryu = "[" + str(self.__class__.__name__) + "] "
        stryu += str(self.__size) + "/" + str(self.__size)
        return stryu
