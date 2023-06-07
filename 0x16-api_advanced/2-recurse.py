#!/usr/bin/python3
""" A module that has a a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the function
should return None
"""
import requests


def recurse(subreddit, after=None, hot_list=None):
    """ A recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should
    return None.
    """
    if hot_list is None:
        hot_list = []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {
            'after': after
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110\
        Safari/537.3"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        query = data['data']['after']
        if data.get(query):
            after = data['data']['after']
            posts = (data['data']['children'])

            for post in posts:
                hot_list.append(post['data']['title'])

            return recurse(subreddit, after, hot_list)
        return (hot_list)
    else:
        return (None)
