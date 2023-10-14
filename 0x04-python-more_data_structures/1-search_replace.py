#!/usr/bin/python3
def search_replace(my_list, search, replace):
    NL = my_list[:]
    for y in range(len(NL)):
        if NL[y] == search:
            NL[y] = replace
    return NL
