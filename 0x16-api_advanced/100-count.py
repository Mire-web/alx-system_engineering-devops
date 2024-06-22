#!/usr/bin/python3
"""
Script to count all keywords provided in a subreddit title list
AUTHOR: Mire-web
"""
import requests
params = {
    'limit': 100,
    'after': None
}
word_count = {}


def count_words(subreddit, word_list):
    headers = {'User-Agent': 'Mirey 1.0 by Mirey'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    try:
        res = requests.get(url, headers=headers,
                           allow_redirects=False, params=params)
        dataset = res.json().get('data').get('children')
        after = res.json().get('after')
        for data in dataset:
            title = [word.lower() for word in
                     data.get('data').get('title').split()]
            for word in word_list:
                word = word.lower()
                if word in title:
                    if word_count.get(word):
                        word_count[word] = word_count[word] + title.count(word)
                    else:
                        word_count[word] = title.count(word)
        if after:
            params['after'] = after
            count_words(subreddit, word_list)
        else:
            sorted_dict = sorted(word_count.items(),
                                 key=lambda item: (-item[1], item[0]))
            for key, item in sorted_dict:
                print('{}: {}'.format(key, item))
    except Exception as e:
        print(e)
        return None
