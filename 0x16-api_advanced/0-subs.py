#!/usr/bin/python3
"""api module"""
import requests

headers = {'User-Agent': 'MyCustomUserAgent/1.0'}


def number_of_subscribers(subreddit):
    """method doc"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
 
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        return 0
