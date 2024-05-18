#!/usr/bin/python3
"""
script takes in a URL, sends a request to the URL and displays the body of the
response decoded in utf-8
"""

import urllib.request as url_req
import urllib.error as url_err
import sys


def fetch_url(url):
    """fetch the body of url"""

    # send GET request to
    req = url_req.Request(url)

    try:
        with url_req.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except url_err.HTTPError as e:
        print('Error code: ', e.code)


if __name__ == "__main__":
    fetch_url(sys.argv[1])
