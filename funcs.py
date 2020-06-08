import os
import json
import time
import pickle
from bs4 import BeautifulSoup
from urllib.request import urlopen


def save(data, path):
    # make proper directories if needed.
    path_split = list(filter(None, path.split('/')))
    if len(path_split) > 1:
        dir = '/'.join(path_split[:-1])
        path = '/'.join(path_split)

        if not os.path.exists(dir):
            os.makedirs(dir, exist_ok=True)

    # if saving json, use json dump.
    if path[-4:] == 'json':
        with open(path, 'w', encoding='UTF8') as f:
            json.dump(data, f, ensure_ascii=False)
    # if not, use pickle dump.
    else:
        with open(path, 'wb') as f:
            pickle.dump(data, f)


def load(path):
    # if loading json, use json load
    if path[-4:] == 'json':
        with open(path, encoding='UTF8') as f:
            result = json.load(f)
    # if not, use pickle load.
    else:
        with open(path, 'rb') as f:
            result = pickle.load(f)

    return result


def get_html(url):
    wait_count = 0
    while wait_count < 5:
        try:
            html = urlopen(url).read().decode('utf-8')
            return html
        except Exception as e:
            print('wait_count = %i, %s' % (wait_count, e))
            wait_count += 1
            time.sleep(10)

    return False


def get_edges(html, mode):
    html_parsed = BeautifulSoup(html, 'html.parser')
    data = html_parsed.find_all("script", {"type": "text/javascript"})
    scripts = ''
    for _data in data:
        if 'window._sharedData =' in str(_data):
            scripts = str(_data)

    json_data = json.loads(scripts.split('window._sharedData =')[1].split(";</script>")[0])

    if mode == 'tag':
        edges = json_data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    elif mode == 'location':
        edges = json_data['entry_data']['LocationsPage'][0]['graphql']['location']['edge_location_to_media']['edges']
    else:
        edges = {}  # TODO

    return edges


def get_res(post):
    res = {}
    node = post['node']

    # post info
    try:
        res['id'] = node['id']
    except IndexError:
        res['id'] = ''

    try:
        res['owner'] = node['owner']['id']
    except IndexError:
        res['owner'] = ''

    try:
        res['taken_at_timestamp'] = node['taken_at_timestamp']
    except IndexError:
        res['taken_at_timestamp'] = ''

    try:
        res['shortcode'] = 'https://www.instagram.com/p/' + node['shortcode']
    except IndexError:
        res['shortcode'] = ''

    try:
        res['text'] = node['edge_media_to_caption']['edges'][0]['node']['text']
    except IndexError:
        res['caption'] = ''

    try:
        res['caption'] = node['edge_media_to_caption']['edges'][0]['node']['text']
    except IndexError:
        res['caption'] = ''

    # media info
    try:
        res['is_video'] = node['is_video']
    except IndexError:
        res['is_video'] = ''

    try:
        res['display_url'] = node['display_url']
    except IndexError:
        res['display_url'] = ''

    return res