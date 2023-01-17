#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
    """

from urllib.request import Request, urlopen
from sys import argv

req = Request(argv[1])
with urlopen(req) as response:
    body = response.headers['X-Request-Id']
    print(body)
