#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers

    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)\
              AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/51.0.2704.103 Safari/537.36'}
    request = requests.get(url, allow_redirects=False, headers=header)
    if request.status_code != 200:
        return 0
    else:
        return request.json()['data']['subscribers']
