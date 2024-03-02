#!/usr/bin/python3
"""A scriscript that takes in a URL and an email address,
-sends a POST request to the passed URL with email as a parameter,
-displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    email = sys.argv[2]

    var = {'email': email}
    resp = requests.post(URL, data=var)

    print("Your email is: {}".format(email))
    print(resp.text)
