#!/usr/bin/python3
"""script that takes your GitHub credentials
  (username & password)
  -uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authentification = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=authentification)
    print(req.json().get("id"))
