#!/usr/bin/python3
"""
Displays GitHub credentials (username and password).
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    username = argv[1]
    password = argv[2]

    Mega_link = "https://api.github.com/user"
    answer = get(Mega_link, auth=(username, password))
    json = answer.json()

    print(json.get('id'))
