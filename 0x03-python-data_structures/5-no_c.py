#!/usr/bin/python3
def no_c(my_string):
    new_s = ""
    for y in my_string:
        if y != 'c' and y != 'C':
            new_s += y
    return new_s
