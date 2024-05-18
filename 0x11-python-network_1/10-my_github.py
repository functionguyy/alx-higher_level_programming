#!/usr/bin/python3
"""script takes your GitHub credentials(username and password) and uses the
GitHub API to display your id
"""
import requests
import sys


def query_GitHub_API(user, psswd):
    """query GitHub API"""

    r = requests.get('https://api.github.com/user', auth=(user, psswd))

    return r


if __name__ == "__main__":
    response = query_GitHub_API(sys.argv[1], sys.argv[2])
    try:
        jd = response.json()
        if len(jd) == 0:
            print("No result")
        else:
            print(jd.get('id'))
    except Exception as e:
        print("Not a valid JSON")
