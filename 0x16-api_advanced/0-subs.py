#!/usr/bin/python3
"""
Script to get subcriber count for reddit
AUTHOR: Mire-web
"""
import requests


def number_of_subscribers(subreddit):
    """Function to return subcriber count"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mirey/1.0'}
    try:
        result = requests.get(url, allow_redirects=False, headers=headers)
        result.raise_for_status()
    except Exception:
        return 0
    return result.json()['data']['subscribers']
