import click
import webbrowser


def show_top_news(top_news):
    for i, article in enumerate(top_news):
        title = article['title']
        source = article['source']['name']
        click.echo('{} {} {}'.format(
            click.style('[{}]'.format(i+1), bold=True),
            title,
            click.style('({})'.format(source), dim=True)
        ))


def open_article(top_news, n):
    article = top_news[n - 1]
    webbrowser.open(article['url'])
