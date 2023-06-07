#!/usr/bin/python3
""" A module that contains a function that uses the Reddit API to retrieve
the number of subscribers for a given subreddit:
"""
import requests


def number_of_subscribers(subreddit):
    """ function that uses the Reddit API to retrieve the number of
    subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110\
        Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except (requests.RequestException, KeyError):
        return 0
