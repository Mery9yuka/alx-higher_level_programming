#!/usr/bin/python3
"""script that takes in a letter
  -sends a POST request to http://0.0.0.0:5000/search_user
  -with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    var = {'q': q}

    try:
        res = requests.post('http://0.0.0.0:5000/search_user', data=var)
        json_dt = res.json()

        if json_dt:
            print("[{}] {}".format(json_dt['id'], json_dt['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
