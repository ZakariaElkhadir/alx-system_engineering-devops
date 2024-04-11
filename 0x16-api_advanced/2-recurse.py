#!/usr/bin/python3

"""api module"""
import requests


def recurse(subreddit, host_list=[]):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        titles = [post['data']['titles'] for post in ['data']['children']]
        return titles
    else:
        return None

