#!/usr/bin/python3
"""api module"""

import requests
import json

def number_of_subscribers(subreddit):
    """doc doc"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)

        subscribers = data["data"]["subscribers"]

        return subscribers
    else:
        return 0
