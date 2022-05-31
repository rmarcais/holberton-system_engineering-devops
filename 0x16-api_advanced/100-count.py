#!/usr/bin/python3
"""
Module that contains the function count_word.
"""

import requests


def count_words(subreddit, word_list):
    """
    Recursive function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Dazzling-Rock-4213'}
    api_url = requests.get(url, headers=headers, allow_redirects=False)
    if api_url.status_code > 300:
        return
