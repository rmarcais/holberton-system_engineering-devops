#!/usr/bin/python3
"""
Module that contains the function number_of_subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {'User-agent': 'Dazzling-Rock-4213'}
    api_url = requests.get(url, headers=user_agent, allow_redirects=False)
    if api_url.status_code > 300:
        return 0
    return(api_url.json().get('data').get('subscribers'))
