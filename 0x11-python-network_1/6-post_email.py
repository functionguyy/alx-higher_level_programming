#!/usr/bin/python3
"""script takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body of the
response
"""
import sys
import requests


def post_email(url, addr):
    """send POST request with data as a parameter"""

    r = requests.post(url, data={'email': addr})

    print(r.text)


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
