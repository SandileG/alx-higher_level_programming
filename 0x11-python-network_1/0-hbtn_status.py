#!/usr/bin/pyhton3

import urllib.request
import sys

# Get the URL from the command-line argument
url = sys.argv[1]

# Open the URL using a with statement for proper resource management
with urllib.request.urlopen(url) as response:
   # Extract the headers from the response
   headers = response.info()

   # Retrieve the X-Request-Id from the headers
   request_id = headers.get("X-Request-Id")

   # Print the retrieved X-Request-Id value
   print(request_id)
