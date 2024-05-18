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
    param = {'q': key}
    r = requests.post(url, data=param)

    return r


if __name__ == "__main__":
    if len(sys.argv) > 1:
        response = query_API(sys.argv[1])
    else:
        response = query_API()

    try:
        jd = response.json()
        if len(jd) == 0:
            print("No result")
        else:
            print("[{}] {}".format(jd.get("id"), jd.get("name")))
    except Exception as e:
            print("Not a valid JSON")
