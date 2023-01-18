#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
    """
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
