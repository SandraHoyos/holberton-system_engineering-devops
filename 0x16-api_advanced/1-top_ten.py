#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints
 the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """
    function that queries the Reddit API and prints
     the titles of the first 10 hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-agent': 'MyHolbertonAPI/0.0.1'}
    request = requests.get(url, allow_redirects=False, headers=header)
    if request.status_code != 200:
        print(None)
    else:
        children = request.json()['data']['children']
        for child in children:
            print(child['data']['title'])
