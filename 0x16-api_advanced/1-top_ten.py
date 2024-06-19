#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints"""

    if not subreddit:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return
    else:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
        return
