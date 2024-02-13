#!/usr/bin/python3
"""
A module to retrieve the number of subscribers for a given subreddit using
the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit. Returns 0 if the
             subreddit is invalid or not found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
