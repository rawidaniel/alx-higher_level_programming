#!/bin/bash
# sends a request to a URL and displays only the status code of the response
curl -sI "$1" | grep "HTTP/" | cut -f2 -d " "
