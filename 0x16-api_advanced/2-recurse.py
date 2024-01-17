#!/usr/bin/python3
"""Recursive function that queries the Reddit
API and returns a list"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """The function"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    hd = {"User-Agent": "My-User-Agent"}
    params = {"after": after}
    r = requests.get(url, headers=hd, params=params, allow_redirects=False)
    if r.status_code == 200:
        data = r.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for child in children:
                    hot_list.append(child["data"]["title"])
                after = data.get("after")
                if after:
                    return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
