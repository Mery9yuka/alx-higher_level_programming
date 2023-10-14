#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == {}:
        return None

    high_value = max(a_dictionary.values())
    if a_dictionary:

        for keys, score in a_dictionary.items():
            if score is high_value:
                return keys
