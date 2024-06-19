#!/usr/bin/python3
"""doc doc"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    headers = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=headers).json()

    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == '__main__':
    """main main"""
    number_of_subscribers(argv[1])
