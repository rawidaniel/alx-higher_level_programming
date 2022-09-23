#!/usr/bin/python3
"""
Module 6-post_email

takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import requests
from sys import argv

if __name__ == "__main__":
    payload = {"email": argv[2]}
    result = requests.post(argv[1], data=payload)
    print(result.text)
