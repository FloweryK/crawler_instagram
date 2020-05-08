import time
import argparse
from urllib.parse import quote
from funcs import *


def crawl(tag, limit):
    # if there's a json file with the same tag, continue from it
    try:
        merged_json = load('results/%s.json' % tag)
        max_id = sorted(merged_json.keys())[-1]
    except FileNotFoundError:
        merged_json = {}
        max_id = ''

    while True:
        # sleep 1 sec to avoid timeout
        time.sleep(1)

        # make url
        url = 'https://www.instagram.com/explore/tags/' + quote(tag)
        url += '/?max_id=' + max_id if max_id else '/'
        print('(%s) opening url: %s' % (tag, url))

        # read url
        html = get_html(url)

        # if there's nothing, break
        if not html:
            print('(%s) timeout' % tag)
            break

        # parse url
        edges = get_edges(html)

        # if there's no update, break
        if len(edges) == 0:
            print('(%s) end of tag' % tag)
            break

        # if # of posts exceeds limit, break
        if len(merged_json) > limit:
            print('(%s) # of posts exceeds limit(%i)' % (tag, limit))
            break

        # merge newly crawled data to the old one
        print('(%s) %i posts to be added (merged_results: %i)' % (tag, len(edges), len(merged_json)))
        for post in edges:
            res = get_res(post)
            max_id = res['id']
            merged_json[res['id']] = res

        # save the result
        save(merged_json, tag + '.json')


if __name__ == '__main__':
    # Argument configuration
    parser = argparse.ArgumentParser()
    parser.add_argument('--tag', type=str, required=True, help='An Instagram tag to crawl')
    parser.add_argument('--limit', type=int, default=1000, help='Post # limit (default=1000). 0 for no limit.')
    args = parser.parse_args()
    tag = args.tag
    limit = args.limit

    # start crawling
    crawl(tag, limit)



