#!/usr/bin/python3
"""
Module that contains the function top_ten.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'User-agent': 'Dazzling-Rock-4213'}
    api_url = requests.get(url, headers=params, allow_redirects=False)
    if api_url.status_code > 300:
        print(None)
        return
    res = api_url.json().get('data').get('children')
    for i in range(10):
        print(res[i].get('data').get('title'))
