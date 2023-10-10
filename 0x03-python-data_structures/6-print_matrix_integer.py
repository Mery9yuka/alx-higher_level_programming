#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        for u in y:
            if u != y[-1]:
                print("{:d}".format(u), end=" ")
            else:
                print("{:d}".format(u), end="")
        print()
