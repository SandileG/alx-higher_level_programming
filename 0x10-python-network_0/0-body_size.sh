#!/bin/bash
# Send request to the URL and retrieve the body size.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
