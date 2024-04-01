#!/usr/bin/python3
"""
Launch request to URL and displays body of the response.
"""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    Mega_link = 'http://0.0.0.0:5000/search_user'
    info = {'q': argv[1] if len(argv) >= 2 else ""}
    answer = post(Mega_link, info)

    type_pet = answer.headers['content-type']

    if type_pet == 'application/json':
        result = answer.json()
        _id = result.get('id')
        name = result.get('name')
        if (result != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
