#!/bin/bash
# send a DELETE request to the URL passed as the first argument
curl -LsX DELETE "$1"
