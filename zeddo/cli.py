"""
zeddo.cli

Command line interface for zeddo.
"""

import sys

import click
import click_config_file

from zeddo.news import get_top_news
from zeddo.config import get_config, set_config
from zeddo.utils import show_top_news, open_article

VERSION = '0.2.0'
CATEGORIES = (
    'business',
    'entertainment',
    'general',
    'health',
    'science',
    'sports',
    'technology'
)


@click.command()
@click.option('-k', '--api-key', help='API key for News API')
@click.option('-l', '--language', default='en',
    help='Filter articles by language')
@click.option('-t', '--category', help='Filter by category')
@click.option('-s', '--search', help='Search by key phrase')
@click.option('-n', '--max-count', default=5, help='Limit number of articles')
@click.version_option(VERSION, '-v', '--version')
@click.help_option('-h', '--help')
@click_config_file.configuration_option('-c', '--config', cmd_name='zeddo')
def top_news(api_key, language, category, search, max_count):
    """
    Fetch and display top news articles.
    """
    # Prompt for API key if not supplied
    if api_key is None:
        api_key = click.prompt('Enter your API key')
        if click.confirm('Save to config file?', default='y'):
            config = get_config()
            config['api_key'] = api_key
            set_config(config)
            print('Saved!\n')

    if category is not None:
        if category not in CATEGORIES:
            click.echo('Invalid category. Valid categories: {}'
                .format(', '.join(CATEGORIES)))

            sys.exit(1)

    # Fetch news
    top_news = get_top_news(api_key, language, category, search, max_count)
    # Display news
    show_top_news(top_news)

    # Prompt for selection and open it in web browser
    i = None
    while True:
        s = click.prompt(
            'Please enter an article number to open',
            default='',
            show_default=False
        )
        # Quit on empty input
        if s == '':
            sys.exit(0)

        # Validate input
        if not s.isnumeric():
            click.echo('{} is not a number!'.format(s))
        else:
            i = int(s)
            if not (0 < i <= len(top_news)):
                click.echo('No such article: {}'.format(i))
            else:
                break

    open_article(top_news, i)


def main():
    top_news(prog_name='zeddo')
