#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    output = []
    for y in my_list:
        output.append(y % 2 == 0)

    return output
