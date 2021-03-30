import random

import requests

# Cache list of all news sources
all_sources = None

def get_sources(api_key):
    url = "https://newsapi.org/v2/sources?apiKey={}".format(api_key)

    response = requests.request("GET", url)
    if response.status_code != 200:
        raise RuntimeError(response.json()['message'])

    return response.json()['sources']

def get_top_news(api_key, n):
    global all_sources
    if all_sources is None:
        all_sources = [source['id'] for source in get_sources(api_key)]

    # Since `sources` (or `country` or `q`) is required, provide all sources.
    url = (
        "https://newsapi.org/v2/top-headlines?" +
        "apiKey={}&".format(api_key) +
        "sources={}&".format(','.join(all_sources)) +
        "pageSize={}".format(n)  # no need for more than n entries
    )

    response = requests.request("GET", url)
    if response.status_code != 200:
        raise RuntimeError(response.json()['message'])

    return response.json()['articles'][:n]
