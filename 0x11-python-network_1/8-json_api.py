#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
    """
if __name__ == "__main__":
    import requests
    from sys import argv
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})
        j = r.json()
        if j:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
