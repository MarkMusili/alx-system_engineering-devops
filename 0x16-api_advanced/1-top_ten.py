#!/usr/bin/python3
"""Print the titles of the first
10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """The function"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        for i in range(10):
            print(r.json().get("data")["children"][i]["data"]["title"])
    else:
        print("None")
