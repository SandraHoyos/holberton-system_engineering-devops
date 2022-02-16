#!/usr/bin/python3
from requests import get
"""
function that queries reddit api and returns number
of subs
"""

def number_of_subscribers(subreddit):
    """
    function definition of getting number of subs
    """
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'my-app/0.0.1'}
    req = get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        return 0
    req = req.json()
    if "data" in req:
        return (req.get("data").get("subscribers"))
    else:
        return 0