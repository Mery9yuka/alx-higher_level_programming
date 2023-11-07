#!/usr/bin/python3
""" function append_write"""


def append_write(filename="", text=""):
    """append a string in the end of a text file """
    with open(filename, "a", encoding="utf8") as textfile:
        return textfile.write(text)
