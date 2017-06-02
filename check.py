#!/usr/bin/env python3
import os
import yaml
import tweepy
from get_tweepy import get_api

filename = 'ids.yaml'
user_id = 870250103004577792 # @xxxx_xxx_george ネタバレアカウント(一部伏せ字)
api = get_api('sakuramochi_pre')

def main():
    data = read_data()

    # check the update of favorites
    ts = api.favorites(user_id=user_id, count=200)
    for t in ts:
        if t.id not in data['favorites']:
            notice_tweet(t)
            add_id('favorites', t.id)

    # check the update of follows
    us = api.friends(user_id=user_id, count=200)
    for u in us:
        if u.id not in data['follows']:
            notice_follow(u)
            add_id('follows', u.id)

def get_url(t):
    return 'https://twitter.com/{}/status/{}'.format(
        t.user.screen_name,
        t.id
    )
    
def notice_tweet(t):
    status = '@skrmch_rhythpri {}'.format(get_url(t))
    api.update_status(status=status)

def notice_follow(u):
    status = '@skrmch_rhythpri https://twitter.com/{}'.format(u.screen_name)
    api.update_status(status=status)
    
def read_data():
    if not os.path.exists(filename):
        data = dict(
            favorites = set(),
            follows = set(),
        )
        with open(filename, 'w') as f:
            yaml.dump(data, f)
    else:
        with open(filename) as f:
            data = yaml.load(f)
    return data

def write_data(data):
    with open(filename, 'w') as f:
        yaml.dump(data, f)

def add_id(key, id):
    data = read_data()
    data[key].add(id)
    write_data(data)
        
if __name__ == '__main__':
    main()
