#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
    """
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    values = {'email': argv[2]}
    data = urlencode(values)
    data = data.encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
