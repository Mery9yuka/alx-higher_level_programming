#!/usr/bin/python3
"""defining a new geometry class"""


class BaseGeometry:
    """ the class BaseGeometry """
    def area(self):
        """No implementation """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ instance that validate a value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
