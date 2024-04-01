#!/usr/bin/python3
"""
Launches request to URL and displays value of variable X-Request-Id
in response header"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    pet = get(argv[1])
    print(pet.headers.get('X-Request-Id'))
