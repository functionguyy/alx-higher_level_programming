#!/usr/bin/python3
"""
script takes in a URL and an email,sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""

import urllib.request as url_req
import urllib.parse as url_parse
import sys


def fetch_url(url, data):
    """
    Sends a POST request to a URL and displays the body of the response decoded
    in utf-8

    Args:
    (url): (str) --> the url to open
    (msg): (str) --> the message request to send
    """

    # send POST request
    req = url_req.Request(url, data)
    with url_req.urlopen(req) as response:
        the_page = response.read()

    decoded_content = the_page.decode('utf-8')

    return decoded_content


if __name__ = "__main__":
    # prepare parameters for POST request
    values = {'email': sys.argv[2]}
    data = url_parse.urlencode(values)
    data = data.encode('ascii')

    # fetch url response object
    response_content = fetch_url(sys.argv[1], data)

    print(response_content)
