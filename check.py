#!/usr/bin/env python3
import os
import yaml
import tweepy
from get_tweepy import get_api

filename = 'ids.yaml'
user_id = 870250103004577792 # @love_mix_george
api = get_api('sakuramochi_pre')

def main():
    ids = read_ids()
    ts = api.favorites(user_id=user_id, count=200)
    for t in ts:
        if t.id not in ids:
            notice(t)
            add_id(t.id)

def get_url(t):
    return 'https://twitter.com/{}/status/{}'.format(
        t.user.screen_name,
        t.id
    )
    
def notice(t):
    status = '@skrmch_rhythpri {}'.format(get_url(t))
    api.update_status(status=status)

def read_ids():
    if not os.path.exists(filename):
        data = set()
        with open(filename, 'w') as f:
            yaml.dump(data, f)
    else:
        with open(filename) as f:
            data = yaml.load(f)
    return data

def add_id(id):
    ids = read_ids()
    ids.add(id)
    with open(filename, 'w') as f:
        yaml.dump(ids, f)
        
if __name__ == '__main__':
    main()
