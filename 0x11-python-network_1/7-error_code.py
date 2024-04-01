#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    linkit = argv[1]

    answer = get(linkit)
    BAD_TXT = 'Error code: {}'
    state = answer.status_code
    print(BAD_TXT.format(state) if (state >= 400) else answer.text)
