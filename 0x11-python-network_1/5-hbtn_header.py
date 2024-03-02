#!/usr/bin/python3
"""script that takes in a URL,
   sends a request to the URLdisplays the X-Request-Id
   header variable of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]

    req = requests.get(URL)
    print(req.headers.get("X-Request-Id"))
