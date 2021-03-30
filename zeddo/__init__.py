import webbrowser
import sys

import click
import click_config_file

from zeddo.news import get_top_news

def show_top_news(top_news):
    for i, article in enumerate(top_news):
        title = article['title']
        source = article['source']['name']
        click.echo("{} {} {}".format(
            click.style("[{}]".format(i+1), bold=True),
            title,
            click.style("({})".format(source), dim=True)
        ))

def open_article(top_news, n):
    article = top_news[n - 1]
    webbrowser.open(article['url'])

@click.command()
@click.option('--api-key', help='API key for News API')
@click.option('--language', default='en')
@click.option('-n', default=5)
@click_config_file.configuration_option(cmd_name='zeddo')
def top_news(api_key, language, n):
    top_news = get_top_news(api_key, language, n)
    show_top_news(top_news)
    n = None
    while True:
        s = click.prompt("Please enter an article number to open", default="")
        if s == '':
            sys.exit(0)

        if not s.isnumeric():
            click.echo("{} is not a number!".format(s))
        else:
            n = int(s)
            if not (0 < n <= len(top_news)):
                click.echo("No such article: {}".format(n))
            else:
                break
    open_article(top_news, n)

if __name__ == '__main__':
    top_news()
