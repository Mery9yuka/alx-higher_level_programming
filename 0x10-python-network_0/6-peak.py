#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function that finds a peak in list of integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    li = 0
    size = len(list_of_integers)
    mid = int(mid)
    mid = ((size - li) // 2) + li
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
