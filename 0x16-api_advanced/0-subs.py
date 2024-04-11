#!/usr/bin/python3
"""api module"""

import requests
import json


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.

    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)

        subscribers = data["data"]["subscribers"]

        return subscribers
    else:
        return 0
