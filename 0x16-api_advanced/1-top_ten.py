#!/usr/bin/python3
"""api module"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyCustomUserAgent/1.0'}
    if subreddit is None:
        return None
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        for i in range(10):
            print(data.get('data').get('children')[i].get('data').get('title'))
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except (ValueError, TypeError) as e:
        print(f"JSON decoding error: {e}")
