#!/bin/bash
# sends a GET request to the URL and display the body of the response
curl -sLH 'X-School-User-Id: 98' "$1"
