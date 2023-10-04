#!/usr/bin/python3
def fizzbuzz():
    for y in range(1, 101):
        if y % 5 == 0 and y % 3 == 0:
            print("FizzBuzz ", end='')
        elif y % 5 == 0:
            print("Buzz ", end='')
        elif y % 3 == 0:
            print("Fizz ", end='')
        else:
            print("{} ".format(y), end="")
            