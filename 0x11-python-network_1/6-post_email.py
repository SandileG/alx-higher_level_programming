#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    
    response = requests.post(url, data={'email': email})
    
    print("Your email is:", email)
    print(response.text)
