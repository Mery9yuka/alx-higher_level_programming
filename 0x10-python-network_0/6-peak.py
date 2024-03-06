#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Function that peak of list_of_integers or None
    """
    size_l = len(list_of_integers)
    mid_e = size_l
    midd = size_l // 2

    if size_l == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (midd < size_l - 1 and
                list_of_integers[midd] < list_of_integers[midd + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            midd = midd + mid_e // 2
        elif mid_e > 0 and list_of_integers[midd] < list_of_integers[midd - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            midd = midd - mid_e // 2
        else:
            return list_of_integers[midd]
