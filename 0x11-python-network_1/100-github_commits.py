#!/usr/bin/python3

"""script that lists the 10 recent commits on a GitHub repo
"""
import requests
import sys

if __name__ == "__main__":
    URL = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(URL)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
