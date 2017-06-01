import os
import yaml
import tweepy
from get_tweepy import get_api

filename = 'ids.yaml'
id = 870250103004577792, # @love_mix_george

def main():
    api = get_api('sakuramochi_pre')
    ids = read_ids()
    fs = api.favorites(id=id, count=200)
    for f in fs:
        if f.id not in ids:
            notice(f)
            add_id(f.id)

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
