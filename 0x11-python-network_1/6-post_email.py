#!/usr/bin/python3
"""A scriscript that takes in a URL and an email address,
-sends a POST request to the passed URL with email as a parameter,
-displays the body of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    URL = sys.argv[1]

    req = urllib.request.Request(URL)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
