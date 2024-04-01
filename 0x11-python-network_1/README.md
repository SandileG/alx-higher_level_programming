## Fetching Internet Resources with Python: urllib and requests

This README provides a guide on how to fetch internet resources using Python packages such as urllib and requests.

## 1. Fetching Internet Resources with the Python Package urllib

Description: urllib is a built-in Python library that allows you to fetch URLs (Uniform Resource Locators) using Python code. It provides several modules for working with URLs, such as urllib.request for opening and reading URLs, urllib.parse for parsing URLs, and urllib.error for handling exceptions raised by urllib.request.

Usage:

import urllib.request

url = 'https://example.com'
response = urllib.request.urlopen(url)
data = response.read()
print(data)

## 2. Decoding urllib Body Response

Description: After fetching a resource using urllib, you may need to decode the response body to work with the data effectively. The response body can be decoded using the .decode() method, specifying the appropriate encoding.

Usage:

decoded_data = data.decode('utf-8')
print(decoded_data)

## 3. Using the Python Package requests

Description: The requests library is a third-party package that simplifies making HTTP requests in Python. It provides a more user-friendly interface compared to urllib.

Usage:

import requests

url = 'https://example.com'
response = requests.get(url)
print(response.text)


## 4. Making HTTP GET Request

Description: To make an HTTP GET request using the requests library, you can use the requests.get() function, passing the URL as an argument.

Usage:

response = requests.get(url)
print(response.text)

5. Making HTTP POST/PUT/etc. Request
Description: Similarly, you can make other types of HTTP requests like POST, PUT, DELETE, etc., using the corresponding functions provided by the requests library (e.g., requests.post(), requests.put()).

Usage:

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, data=payload)
print(response.text)

## 6. Fetching JSON Resources

Description: If the fetched resource is in JSON format, you can directly parse it into a Python dictionary using the .json() method provided by the requests library.

Usage:

response = requests.get(url)
json_data = response.json()
print(json_data)

## 7. Manipulating Data from an External Service

Description: Once you've fetched data from an external service, you can manipulate it according to your requirements using standard Python data manipulation techniques.

Usage: (Example manipulating JSON data)

# Assuming 'json_data' is fetched JSON data
for item in json_data['items']:
    print(item['name'])
