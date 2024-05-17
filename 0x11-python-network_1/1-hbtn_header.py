#!/usr/bin/python3
"""script takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response"""
import urllib.request as url_req
import sys


def fetch_url(url):
    """fetch a url"""

    req = url_req.Request(url)
    with url_req.urlopen(req) as response:
        headers = response.headers

    return headers


if __name__ == "__main__":
    headers = fetch_url(sys.argv[1])
    print(headers.get('X-Request-Id'))
