#!/bin/bash
# sends a request to a URL as an argument, and displays only the status code
curl -sLw '%{response_code}' "$1" -o /dev/null
