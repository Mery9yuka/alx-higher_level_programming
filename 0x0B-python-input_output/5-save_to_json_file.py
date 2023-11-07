#!/usr/bin/python3
"""function that writes an object to
text file, using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """save to JSON file object to textfile """
    with open(filename, 'w') as textfile:
        return textfile.write(json.dumps(my_obj))
