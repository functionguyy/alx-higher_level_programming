#!/usr/bin/python3
"""
script takes in a URL, sends a request to the URL and displays the body of
the response
"""
import requests
import sys


def fetch_url_response(url):
    """sends a request to the URL and displays the body of the response"""

    r = requests.get(url)

    return r


if __name__ == "__main__":
    response = fetch_url_response(sys.argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
