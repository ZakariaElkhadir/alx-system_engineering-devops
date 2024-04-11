import requests

#!/usr/bin/python3

"""api module"""


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        titles = [post['data']['title'] for post in data['data']['children']]
        return titles
    else:
        return None
