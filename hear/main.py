import click
import click_config_file

from news import get_top_news

@click.command()
@click.option('--api-key', help='API key for News API')
@click.option('-n', default=5)
@click_config_file.configuration_option()
def top_news(api_key, n):
    top_news = get_top_news(api_key, n)

if __name__ == '__main__':
    top_news()
