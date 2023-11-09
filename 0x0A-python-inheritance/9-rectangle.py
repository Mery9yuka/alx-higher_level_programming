#!/usr/bin/python3
"""
    Implement the BaseGeometry class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherite by BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height
        
        def area(self):
         """Returns an area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return a rectangle description: width and height"""
        str_1 = "[" + str(self.__class__.__name__) + "] "
        str_1 += str(self.__width) + "/" + str(self.__height)
        return str_1
