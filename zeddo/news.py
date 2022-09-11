"""
zeddo.news

Fetch news articles from News API.
"""

import requests

# Cache list of all news sources
all_sources = None


def get_sources(api_key):
    """
    Get a list of all news sources.

    :param api_key: API key for News API
    :type api_key: str
    :return: List of news sources
    :rtype: list
    :raises RuntimeError: If API request fails
    """
    url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key)

    response = requests.request('GET', url)
    if response.status_code != 200:
        raise RuntimeError(response.json()['message'])

    return response.json()['sources']


def get_top_news(api_key, language, category, query, n):
    """
    Get top news articles.

    :param api_key: API key for News API
    :type api_key: str
    :param language: Filter articles by language
    :type language: str
    :param category: Filter by category
    :type category: str
    :param query: Search by key phrase
    :type query: str
    :param n: Limit number of articles
    :type n: int
    :return: List of top news articles
    :rtype: list
    :raises RuntimeError: If API request fails
    """
    global all_sources
    if all_sources is None:
        all_sources = [source['id'] for source in get_sources(api_key)]

    # Since `sources` (or `country` or `q`) is required, provide all sources.
    url = (
        'https://newsapi.org/v2/top-headlines?' +
        'apiKey={}&'.format(api_key) +
        'language={}&'.format(language) +
        # Cannot provide both `sources` and `category` for whatever reason
        ('sources={}&'.format(','.join(all_sources)) if not category else '') +
        ('category={}&'.format(category) if category else '') +
        ('q={}&'.format(query) if query else '') +
        'pageSize={}'.format(n)  # no need for more than n entries
    )

    response = requests.request('GET', url)
    if response.status_code != 200:
        raise RuntimeError(response.json()['message'])

    articles = response.json()['articles']
    return articles[:n] if n < len(articles) else articles
