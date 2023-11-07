#!/usr/bin/python3
""" function that
return an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """return a object represented by JSON string to a PYTHON data"""
    return json.loads(my_str)
