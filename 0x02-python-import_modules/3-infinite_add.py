#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    S = 0
    if len(sys.argv) > 1:
        for y in sys.argv[1:]:
            S += int(y)
        print(S)
    else:
        print("0")
