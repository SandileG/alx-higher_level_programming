#!/bin/bash
# This script takes in a URL, sends a request to that URL using curl,
# and displays the size of the response body in bytes.

# Send request to the URL and retrieve the body size.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
