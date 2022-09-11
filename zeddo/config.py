import os.path
import click
import toml

CONFIG_PATH = os.path.join(
    click.get_app_dir(app_name='zeddo'),
    'config'
)


def get_config():
    with open(CONFIG_PATH, 'r') as c:
        return toml.load(c)


def set_config(config):
    with open(CONFIG_PATH, 'w+') as c:
        toml.dump(config, c)
