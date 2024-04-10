#!/usr/bin/python3
"""api module"""
import requests

headers = {'User-Agent': 'MyCustomUserAgent/1.0'}


def number_of_subscribers(subreddit):
    """method doc"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad status codes
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 0
    except (ValueError, TypeError) as e:  # Handles JSON decoding errors
        print(f"JSON decoding error: {e}")
        return 0
