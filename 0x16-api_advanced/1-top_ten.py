#!/usr/bin/python3
""" A module that has a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ A function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {
        'limit': 10
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110\
        Safari/537.3"
    }
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print("None")
