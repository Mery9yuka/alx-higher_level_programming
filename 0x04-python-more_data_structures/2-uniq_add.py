#!/usr/bin/python3
def uniq_add(my_list=[]):

    NL = []
    result = 0
    for y in my_list:

        if y not in NL:
            result += y
            NL.append(y)

    return result
