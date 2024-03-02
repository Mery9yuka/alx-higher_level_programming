#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""
import sys
import urllib.request

if __name__ == "__main__":
    URL = sys.argv[1]

    req = urllib.request.Request(URL)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
