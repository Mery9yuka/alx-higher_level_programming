#!/usr/bin/python3
"""function that write string in a textfile"""


def write_file(filename="", text=""):
    """ write a string in a textfile
        Returns: number of characters written in a textfile
    """
    with open(filename, "w", encoding="utf-8") as textfile:
        return textfile.write(text)
