#!/usr/bin/env bash
# curling the server then filtering to only get the number
echo "$(curl -s -w '%{size_download}' -o /dev/null "$1")"
