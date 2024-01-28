#!/bin/bash
# sends a POST request to the passed URL and displays body of the response
curl -sL -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
