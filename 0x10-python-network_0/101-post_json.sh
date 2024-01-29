#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -sL --json "@$2" "$1"
