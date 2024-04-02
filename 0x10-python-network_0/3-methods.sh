#!/bin/bash
# Sends an OPTIONS request to the URL  and retrieves the Allow header
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -d ' ' -f 2-
