#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for y in range(list_length):
        result = 0
        try:
            result = my_list_1[y] / my_list_2[y]

        except (TypeError, ValueError):
            result = 0
            print("wrong type")

        except ZeroDivisionError:
            result = 0
            print("division by 0")

        except IndexError:
            result = 0
            print("out of range")

        finally:
            n_list.append(result)

    return n_list
