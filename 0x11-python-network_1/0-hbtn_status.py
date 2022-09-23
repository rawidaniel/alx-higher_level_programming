"""
Module 0-hbtn_status
fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as req:
    respo = req.read()
    cls = type(respo)
    data = respo.decode('UTF-8')
    print("Body response:")
    print(f"    - type: {cls}")
    print(f"    - content: {respo}")
    print(f"    - utf8 content: {data}")