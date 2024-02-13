#!/usr/bin/python3
"""
A module containing a recursive function to query the Reddit API and
retrieve the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): A list to store the titles of hot articles.
                                   Defaults to None.
        after (str, optional): Parameter to paginate through the results.
                               Defaults to None.

    Returns:
        list or None: A list containing the titles of all hot articles for the
                      given subreddit. Returns None if no results are found or
                      if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))

        after = data.get('data').get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
