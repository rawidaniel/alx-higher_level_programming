#!/usr/bin/python3
"""
Module 0-hbtn_status
fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as req:
        respo = req.read()
        type_of_class = type(respo)
        data = respo.decode('UTF-8')
        print("Body response:")
        print(f"\t- type: {type_of_class}")
        print(f"\t- content: {respo}")
        print(f"\t- utf8 content: {data}")
