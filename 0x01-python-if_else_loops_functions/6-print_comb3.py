#!/usr/bin/python3
for a in range(0, 10):
    for i in range(a + 1, 10):
        if a == 8 and i == 9:
            print("{}{}".format(a, i))
        else:
            print("{}{}".format(a, i), end=", ")
