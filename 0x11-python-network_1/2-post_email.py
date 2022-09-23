#!/usr/bin/python3
"""
Module 2-post_email.py

takes in a URL and an email, sends a POST request to the passed URL 
with the email as a parameter, and displays the body of the response 
(decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

values = {"email": sys.argv[2]}
url = sys.argv[1]
data = urllib.parse.urlencode(values)
data = data.encode("ascii")
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as respon:
    print(respon.read().decode('UTF-8'))
