#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:

        for y in sorted(a_dictionary):
            print("{}: {}".format(y, a_dictionary[y]))
