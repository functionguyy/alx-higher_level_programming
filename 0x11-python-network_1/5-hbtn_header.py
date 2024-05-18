#!/usr/bin/python3
"""script takes in a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""
import sys
import requests


def fetch_url(url):
    """get response from server"""

    r = requests.get(url)

    return r


if __name__ == "__main__":
    response = fetch_url(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
