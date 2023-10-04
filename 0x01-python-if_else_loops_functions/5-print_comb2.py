#!/usr/bin/python3
for y in range(0, 100):
    if y == 99:
        print("{}".format(y))
    else:
        print("{:01}".format(y), end=", ")