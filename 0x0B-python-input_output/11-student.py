#!/usr/bin/python3
"""creates  a Student class """

class Student:
    """ Retrieves a dictionary representation of student instance"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of student instance"""
        if (type(attrs) == list and
                all(type(items) == str for items in attrs)):
            return {y: getattr(self, y) for y in attrs if hasattr(self, y)}

        return self.__dict__

    def reload_from_json(self, json):
        """Function that replaces all attributes of the student"""
        for y, u in json.items():
            setattr(self, y, u)
