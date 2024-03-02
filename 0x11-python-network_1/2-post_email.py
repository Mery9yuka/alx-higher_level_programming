#!/usr/bin/python3
"""script that takes in a URL and an email
   -sends a POST request to the passed URL with email as a parameter
   -displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    val = {"email": sys.argv[2]}
    var = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(URL, var)
    with urllib.request.urlopen(req) as Response:
        print(Response.read().decode("utf-8"))
