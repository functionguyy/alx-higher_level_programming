#!/usr/bin/python3
"""
script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with letter as a paramter
"""
import sys
import requests


def query_API(key=""):
    """send a POST request"""

    url = "http://0.0.0.0:5000/search_user"
    param = key
    r = requests.post(url, data=param)

    return r


if __name__ == "__main__":
    if len(sys.argv) > 1:
        response = query_API(sys.argv[1])
    else:
        response = query_API()

    if response.status_code != 204:
        try:
            jd = response.json()
            print("[{}] {}".format(jd.get("id"), jd.get("name")))
        except JSONDecodeError as e:
            print("Not a valid JSON")
    else:
        print("No result")
