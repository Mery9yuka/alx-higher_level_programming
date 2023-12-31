#!/usr/bin/python3
"""scripts adding all arguments to a Python list, then saving them to file"""

from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file \
        = __import__('6-load_from_json_file').load_from_json_file

tfile = "add_item.json"

try:
    item = load_from_json_file(tfile)
except FileNotFoundError:
    item = []

for arg in argv[1:]:
    item.append(arg)

save_to_json_file(item, tfile)
