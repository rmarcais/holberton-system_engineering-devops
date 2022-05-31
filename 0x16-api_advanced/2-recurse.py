#!/usr/bin/python3
"""
Module that contains the function recurse.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function
    should return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    ua = {'User-agent': 'Dazzling-Rock-4213'}
    params = {'after': after}
    api_url = requests.get(url, headers=ua, params=params,
                           allow_redirects=False)
    if api_url.status_code > 300:
        return None
    res = api_url.json().get('data').get('children')
    after = api_url.json().get('data').get('after')
    for items in res:
        hot_list.append(items.get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
