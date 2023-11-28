#!/usr/bin/python3
"""Defining a function of text-indentation."""


def text_indentation(text):
    """Print a text with 2 new lines after each of these char -> '.', '?', and ':'.
    Raises:
        TypeError: If text isn't a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t = 0
    while t < len(text) and text[t] == ' ':
        t += 1

    while t < len(text):
        print(text[t], end="")
        if text[t] == "\n" or text[t] in ".?:":
            if text[t] in ".?:":
                print("\n")
                t += 1
                while t < len(text) and text[t] == ' ':
                    t += 1
                continue
        t += 1
