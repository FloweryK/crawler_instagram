import time
import argparse
from urllib.parse import quote
from funcs import *


def crawl(mode, target, limit):
    # query
    query = ''
    if mode == 'tag':
        query += 'tags/' + target
    elif mode == 'location':
        query += 'locations/' + target
    else:
        print('Invalid mode:', mode)

    # if there's a json file with the same query, continue from it
    try:
        merged_json = load('results/' + query + '.json')
        max_id = sorted(merged_json.keys())[-1]
    except FileNotFoundError:
        merged_json = {}
        max_id = ''

    while True:
        # sleep 1 sec to avoid timeout
        time.sleep(1)

        # make url
        url = 'https://www.instagram.com/explore/' + quote(query)
        url += '/?max_id=' + max_id if max_id else '/'
        print('(%s) opening url: %s' % (query, url))

        # read url
        html = get_html(url)
        if not html:
            print('(%s) timeout' % query)
            break

        # parse url
        edges = get_edges(html, mode)
        if len(edges) == 0:
            print('(%s) end of query' % query)
            break

        # if # of posts exceeds limit, break
        if len(merged_json) > limit:
            print('(%s) # of posts exceeds limit (%i)' % (query, limit))
            break

        # merge newly crawled data to the old one
        print('(%s) %i posts to be added (merged_results: %i)' % (query, len(edges), len(merged_json)))
        for post in edges:
            res = get_res(post)
            max_id = res['id']
            merged_json[res['id']] = res

        # save the result
        save(merged_json, 'result/' + query + '.json')


if __name__ == '__main__':
    # Argument configuration
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, required=True, help='crawling mode among: tag, locationid')
    parser.add_argument('--target', type=str, required=True, help='crawling target')
    parser.add_argument('--limit', type=int, default=1000, help='Post # limit (default=1000). 0 for no limit.')
    args = parser.parse_args()
    mode = args.mode
    target = args.target
    limit = args.limit

    # start crawling
    crawl(mode, target, limit)



