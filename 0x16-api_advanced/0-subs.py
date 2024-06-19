#!/usr/bin/python3
"""
Script to get subcriber count for reddit
AUTHOR: Mire-web
"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'subs'}
    try:
        result = requests.get(url, headers=headers, allow_redirects=False)
        result.raise_for_status()
    except Exception:
        return 0
    return result.json()['data']['subscribers']
