#!/usr/bin/python3
def roman_to_int(roman_string):

    if (not isinstance(roman_string, str) or roman_string == ""):
        return 0

    rom_dic = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100,
        "D": 500, "M": 1000
    }
    i = 0

    for y in range(len(roman_string)):
        if rom_dic.get(roman_string[y], 0) == 0:
            return 0
        if (y != (len(roman_string) - 1)) and\
            rom_dic[roman_string[y]] < rom_dic[roman_string[y + 1]]:
            i += rom_dic[roman_string[y]] * -1

        else:
            i += rom_dic[roman_string[y]]

    return i
