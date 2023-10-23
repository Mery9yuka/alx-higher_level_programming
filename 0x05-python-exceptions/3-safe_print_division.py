#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        results = a / b
        print("Inside result: {}".format(results))
        return (results)

    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return (None)
