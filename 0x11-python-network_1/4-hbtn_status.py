#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status using requests
library"""
import requests


def fetch_url(url):
    """get response from server"""

    r = requests.get(url)

    return r


if __name__ == "__main__":
    response = fetch_url("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
