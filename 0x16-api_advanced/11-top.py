#!/usr/bin/python3
"""
Script to get top_ten hot topics on a subreddit
AUTHOR: Mire-web
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints top ten topics
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mirey/1.0'}
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        response.raise_for_status()
        result = response.json().get('data').get('children')
        titles = [data.get('data').get('title') for data in result]
        for title in titles:
            print(title)
    else:
        print(None)
