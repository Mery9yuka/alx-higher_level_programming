#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    max = my_list[0]

    for y in range(len(my_list)):
        if max < my_list[y]:
            max = my_list[y]
    return max
