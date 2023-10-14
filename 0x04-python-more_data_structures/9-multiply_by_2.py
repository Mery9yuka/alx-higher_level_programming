#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict = a_dictionary.copy()
    for y in dict.keys():
        dict[y] *= 2
    return dict