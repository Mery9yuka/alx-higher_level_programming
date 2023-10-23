#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for y in range(list_length):
        results = 0
        try:
            result = my_list_1[y] / my_list_2[y]
        except (TypeError, ValueError):
            results = 0
            print("wrong type")

        except ZeroDivisionError:
            results = 0
            print("division by 0")

        except IndexError:
            results = 0
            print("out of range")

        finally:
            my_list_3.append(results)

    return my_list_3
