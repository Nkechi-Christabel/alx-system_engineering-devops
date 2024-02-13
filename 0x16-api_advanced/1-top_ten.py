#!/usr/bin/python3
"""
A module to retrieve and print the titles of the first 10 hot posts for a given
subreddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            print(post['data']['title'])
    else:
        print("None")
