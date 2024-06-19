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
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Google Chrome Version 125.0.6422.142 '}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        result = response.json().get('data').get('children')
        titles = [data.get('data').get('title') for data in result]
        for title in titles:
            print(title)
    except requests.exceptions.RequestException as req_err:
        print(None)
