#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    LD = number % 10
    print(LD, end='')
    return LD
