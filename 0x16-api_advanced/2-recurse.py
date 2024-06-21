
#!/usr/bin/python3
"""
Script to recursively return list containing the title of all hot articles for a subreddit
"""
import requests
params = {
    'limit': 100,
    'after': None
}


def recurse(subreddit, hot_list=[]):
    """Recursive function to retrieve all reddit hot articles in a subreddit"""
    headers = {'User-Agent': 'Mirey 1.0 by mirey'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    try:
        res = requests.get(url, headers=headers, params=params, allow_redirects=False)
        after = res.json().get('data').get('after')
        data_set = res.json()['data']['children']
        for data in data_set:
            hot_list.append(data['data']['title'])
        if not after:
            return hot_list
        else:
            params['after'] = after
            return recurse(subreddit, hot_list)
    except Exception as e:
        return None
