#!/usr/bin/python3
"""function that read from a file"""


def read_file(filename=""):
    """ read file and print its content to stdout"""
    with open(filename, "r", encoding='utf-8') as textfile:
        print(textfile.read(), end="")
