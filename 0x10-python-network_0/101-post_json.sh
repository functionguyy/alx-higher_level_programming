#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -sLH "Accept: " --json "@$2" "$1"
