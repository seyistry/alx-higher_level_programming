#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
    """
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers["X-Request-Id"])
