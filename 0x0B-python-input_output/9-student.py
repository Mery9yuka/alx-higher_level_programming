#!/usr/bin/python3
"""it's a Student class """


class Student:
    """ Retrieves a dictionary representation of  student instance"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of  student instance"""
        return self.__dict__
