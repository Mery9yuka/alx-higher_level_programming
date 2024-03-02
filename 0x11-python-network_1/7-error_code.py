#!/usr/bin/python3

"""script that takes in a URL,
   sends a request to the URL
   displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]

    resp = requests.get(URL)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
