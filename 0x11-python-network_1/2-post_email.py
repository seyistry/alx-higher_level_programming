#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
    """
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv

    req = Request(argv[1])
    with urlopen(req) as response:
        print(response.headers['X-Request-Id'])
