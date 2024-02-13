#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries the Reddit API to count occurrences of given keywords
    in the titles of hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count occurrences of in the
                          titles.
        counts (dict, optional): A dictionary to store the counts of each
                                 keyword. Defaults to None.
        after (str, optional): Parameter to paginate through the results.
                               Defaults to None.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')('children')
        for post in data:
            title = post.get('data').get('title')
            for word in word_list:
                if word.lower() in title.lower().split():
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        after = data.get('data').get('after')
        if after:
            count_words(subreddit, word_list, counts, after)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no matching posts found.")
