#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status using
   urllib
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        cont = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
        print("\t- utf8 content: {}".format(cont.decode('utf-8')))
