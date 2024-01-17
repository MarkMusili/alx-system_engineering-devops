#!/usr/bin/python3
"""Module to query the Reddit API
and returns the number of subscribers
or 0 if an invalid subreddit is given."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get("data")["subscribers"]
    return 0
