#!/bin/bash
# displays all HTTP methods the server will accept
curl -sLIX "OPTIONS" "$1" | grep -e 'Allow' | cut -d " " -f1 --complement
