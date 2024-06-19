#!/usr/bin/python3
'''recurse module'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing
      the titles of all hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "subreddit-recurse-script/1.0"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            #  Titles of the hot posts are extracted from
            # the children field and added to hot_list.
            hot_list.extend([post["data"]["title"]
                             for post in data.get("children", [])])
            next_after = data.get("after", None)
            if next_after:
                return recurse(subreddit, hot_list, next_after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except Exception:
        return None
