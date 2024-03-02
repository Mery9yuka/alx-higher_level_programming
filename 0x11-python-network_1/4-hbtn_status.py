#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    URL = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(URL)

    print("Body response:")
    print("\t- type:", type(resp.text))
    print("\t- content:", resp.text)

